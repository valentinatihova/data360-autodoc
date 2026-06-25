"""Shared HTTP helpers for the Data 360 Connect REST API clients.

All ``/ssot/*`` fetchers share the same needs: a bearer-authenticated GET with
exponential-backoff retry, and ``nextPageUrl`` pagination with a cycle guard.
Centralizing them here keeps the per-endpoint clients (``metadata.py``,
``streams.py``) small and consistent.
"""

from __future__ import annotations

import time
from typing import Any, Final, Iterator

import requests

_MAX_ATTEMPTS: Final = 3
_BACKOFF_BASE_SECONDS: Final = 1.0


class FetchError(RuntimeError):
    """Raised when a Data 360 API request fails (4xx, or retries exhausted)."""


def get_json(url: str, *, access_token: str, timeout: float) -> Any:
    """GET ``url`` with bearer auth, retrying transient failures.

    Retries transport errors and 5xx responses up to three times with
    exponential backoff (1s, 2s, 4s). 4xx responses are terminal.

    Args:
        url: Absolute URL to request.
        access_token: OAuth bearer token.
        timeout: Per-request timeout in seconds.

    Returns:
        The decoded JSON body.

    Raises:
        FetchError: On a 4xx response or after exhausting retries.
    """
    headers = {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}
    last_error: str | None = None
    for attempt in range(_MAX_ATTEMPTS):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
        except requests.RequestException as exc:
            last_error = str(exc)
        else:
            if response.status_code == 200:
                try:
                    return response.json()
                except ValueError as exc:
                    # A 200 with a non-JSON body (e.g. a proxy/login HTML page)
                    # must become a FetchError, not leak a raw JSONDecodeError
                    # past the CLI's clean-error handler.
                    raise FetchError(
                        f"Non-JSON 200 response from {url}: {exc}"
                    ) from exc
            if 400 <= response.status_code < 500:
                raise FetchError(
                    f"Request rejected ({response.status_code}) for {url}: "
                    f"{response.text[:500]}"
                )
            last_error = f"HTTP {response.status_code}: {response.text[:500]}"
        if attempt < _MAX_ATTEMPTS - 1:
            time.sleep(_BACKOFF_BASE_SECONDS * (2**attempt))
    raise FetchError(
        f"Request to {url} failed after {_MAX_ATTEMPTS} attempts: {last_error}"
    )


def iter_pages(
    first_url: str, *, base_url: str, access_token: str, timeout: float
) -> Iterator[dict[str, Any]]:
    """Yield each page of a paginated ``/ssot/*`` response.

    Follows each page's ``nextPageUrl`` (absolute or relative) until exhausted,
    guarding against a self-referential or repeating link that would otherwise
    loop forever.

    Args:
        first_url: Absolute URL of the first page.
        base_url: Org base URL, used to resolve relative ``nextPageUrl`` values.
        access_token: OAuth bearer token.
        timeout: Per-request timeout in seconds.

    Yields:
        Each page's decoded JSON body.

    Raises:
        FetchError: On a request failure or a detected pagination cycle.
    """
    seen: set[str] = set()
    next_url: str | None = first_url
    while next_url:
        if next_url in seen:
            raise FetchError(f"Pagination cycle detected at {next_url}")
        seen.add(next_url)
        page = get_json(next_url, access_token=access_token, timeout=timeout)
        yield page
        next_url = _resolve_next(page.get("nextPageUrl"), base_url)


def _resolve_next(raw: Any, base_url: str) -> str | None:
    """Normalize a ``nextPageUrl`` value to an absolute URL, or ``None``."""
    if not raw or not isinstance(raw, str):
        return None
    if raw.startswith("http://") or raw.startswith("https://"):
        return raw
    return f"{base_url.rstrip('/')}/{raw.lstrip('/')}"
