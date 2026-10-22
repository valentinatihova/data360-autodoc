"""Borrow an org's session from the Salesforce CLI (``sf``).

``generate --target-org ALIAS`` reuses an org the user already authorized with
``sf org login web --alias ALIAS``, so no connected app or JWT key is needed.
The access token never leaves this module in a message: errors carry only the
alias and the ``sf`` error text.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from typing import Final

#: How long ``sf org display`` may take (it can refresh the session first).
SF_TIMEOUT_SECONDS: Final = 60


class SfCliError(RuntimeError):
    """``sf`` is missing, failed, or returned no usable session."""


def org_credentials(alias: str) -> tuple[str, str]:
    """Return ``(instance_url, access_token)`` for an org authorized in ``sf``.

    Raises:
        SfCliError: With a one-line, token-free message the CLI can print.
    """
    sf = shutil.which("sf")  # finds sf.cmd on Windows too
    if sf is None:
        raise SfCliError(
            "Salesforce CLI (sf) not found on PATH. Install it from "
            "https://developer.salesforce.com/tools/salesforcecli, then run "
            f"`sf org login web --alias {alias}`."
        )
    try:
        completed = subprocess.run(
            [sf, "org", "display", "--target-org", alias, "--json"],
            capture_output=True,
            text=True,
            timeout=SF_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise SfCliError(
            f"`sf org display` did not answer within {SF_TIMEOUT_SECONDS} s."
        ) from exc
    except OSError as exc:
        raise SfCliError(f"Could not run sf: {exc.strerror or exc}") from exc

    body = _parse_json(completed.stdout)
    result = body.get("result")
    if not isinstance(result, dict):
        result = {}
    url, token = result.get("instanceUrl"), result.get("accessToken")
    if completed.returncode != 0 or not url or not token:
        reason = body.get("message") or "no access token in its output"
        raise SfCliError(
            f"sf could not provide a session for '{alias}': {reason} "
            f"Run `sf org login web --alias {alias}`."
        )
    return url, token


def _parse_json(stdout: str) -> dict:
    """Parse ``sf --json`` output, which may be preceded by warning lines."""
    start = stdout.find("{")
    if start == -1:
        return {}
    try:
        data = json.loads(stdout[start:])
    except ValueError:
        return {}
    return data if isinstance(data, dict) else {}
