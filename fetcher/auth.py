"""OAuth 2.0 JWT Bearer Flow for Salesforce Data 360.

This module performs the server-to-server JWT bearer flow only (per project
policy: never store user passwords or client secrets). The caller supplies a
connected-app ``client_id``, the path to the app's private key, and the
``username`` to impersonate; we mint a short-lived signed assertion and exchange
it for an access token.

Reference: https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_jwt_flow.htm
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Final

import jwt
import requests

#: OAuth grant type identifier for the JWT bearer flow.
_GRANT_TYPE: Final = "urn:ietf:params:oauth:grant-type:jwt-bearer"
#: Audience for production logins.
AUD_PRODUCTION: Final = "https://login.salesforce.com"
#: Audience for sandbox / scratch-org logins.
AUD_SANDBOX: Final = "https://test.salesforce.com"
#: Default token endpoint for production JWT bearer exchange.
DEFAULT_TOKEN_URL: Final = "https://login.salesforce.com/services/oauth2/token"
#: Token endpoint for sandbox / scratch-org JWT bearer exchange.
SANDBOX_TOKEN_URL: Final = "https://test.salesforce.com/services/oauth2/token"
#: Assertion lifetime in seconds (Salesforce caps this at 3 minutes).
_ASSERTION_TTL_SECONDS: Final = 180
#: Number of token-exchange attempts before giving up.
_MAX_ATTEMPTS: Final = 3
#: Base delay (seconds) for exponential backoff: 1s, 2s, 4s.
_BACKOFF_BASE_SECONDS: Final = 1.0


class AuthError(RuntimeError):
    """Raised when the JWT bearer token exchange ultimately fails."""


def build_assertion(
    *,
    client_id: str,
    username: str,
    private_key: str,
    audience: str = AUD_PRODUCTION,
    now: int | None = None,
) -> str:
    """Build and sign the JWT assertion for the bearer flow.

    Args:
        client_id: The connected app's consumer key (``iss`` claim).
        username: The Salesforce username to impersonate (``sub`` claim).
        private_key: PEM-encoded RSA private key contents used to sign (RS256).
        audience: Token endpoint audience; use :data:`AUD_PRODUCTION` or
            :data:`AUD_SANDBOX`.
        now: Override for the current epoch seconds (used in tests for
            deterministic ``exp`` claims).

    Returns:
        The encoded, signed JWT assertion as a compact string.
    """
    issued_at = int(time.time()) if now is None else now
    claims = {
        "iss": client_id,
        "sub": username,
        "aud": audience,
        "exp": issued_at + _ASSERTION_TTL_SECONDS,
    }
    return jwt.encode(claims, private_key, algorithm="RS256")


def get_access_token(
    *,
    instance_url: str,
    client_id: str,
    private_key_path: str,
    username: str,
    token_url: str = DEFAULT_TOKEN_URL,
    audience: str = AUD_PRODUCTION,
    timeout: float = 30.0,
) -> dict[str, str]:
    """Obtain an access token via the JWT bearer flow.

    Retries the token exchange up to three times with exponential backoff
    (1s, 2s, 4s) on transient transport errors or 5xx responses. Client errors
    (4xx) are treated as terminal and surfaced immediately.

    Args:
        instance_url: Base URL of the Salesforce org (e.g.
            ``https://mydomain.my.salesforce.com``). Used as the fallback
            ``instance_url`` in the return value when the org does not echo one.
        client_id: The connected app's consumer key.
        private_key_path: Filesystem path to the PEM private key.
        username: The Salesforce username to impersonate.
        token_url: The OAuth token endpoint to POST the assertion to. Defaults
            to :data:`DEFAULT_TOKEN_URL`
            (``https://login.salesforce.com/services/oauth2/token``). **Sandbox
            and scratch orgs must override this** with
            :data:`SANDBOX_TOKEN_URL`
            (``https://test.salesforce.com/services/oauth2/token``).
        audience: JWT ``aud`` claim; :data:`AUD_PRODUCTION` (default) or
            :data:`AUD_SANDBOX` for sandboxes. Should match ``token_url``.
        timeout: Per-request timeout in seconds.

    Returns:
        A dict with ``access_token`` and ``instance_url`` keys. The
        ``instance_url`` reflects the value returned by Salesforce when present
        (it may differ from the input), otherwise the input value.

    Raises:
        FileNotFoundError: If ``private_key_path`` does not exist.
        AuthError: If the token exchange fails after all retries, the org
            returns a non-retryable error, or the success response is missing
            ``access_token``.
    """
    private_key = Path(private_key_path).read_text(encoding="utf-8")
    assertion = build_assertion(
        client_id=client_id,
        username=username,
        private_key=private_key,
        audience=audience,
    )
    data = {"grant_type": _GRANT_TYPE, "assertion": assertion}

    last_error: str | None = None
    for attempt in range(_MAX_ATTEMPTS):
        try:
            response = requests.post(token_url, data=data, timeout=timeout)
        except requests.RequestException as exc:  # transport-level failure
            last_error = str(exc)
        else:
            if response.status_code == 200:
                body = response.json()
                try:
                    access_token = body["access_token"]
                except KeyError as exc:
                    raise AuthError(
                        "Unexpected response: access_token not found"
                    ) from exc
                return {
                    "access_token": access_token,
                    "instance_url": body.get("instance_url", instance_url),
                }
            # 4xx: bad assertion / config — retrying will not help.
            if 400 <= response.status_code < 500:
                raise AuthError(
                    f"JWT bearer exchange rejected ({response.status_code}): "
                    f"{response.text}"
                )
            last_error = f"HTTP {response.status_code}: {response.text}"

        # Back off before the next attempt, but never after the final one.
        if attempt < _MAX_ATTEMPTS - 1:
            time.sleep(_BACKOFF_BASE_SECONDS * (2**attempt))

    raise AuthError(
        f"JWT bearer exchange failed after {_MAX_ATTEMPTS} attempts: {last_error}"
    )
