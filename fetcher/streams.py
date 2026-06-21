"""Data Stream / DLO schema fetcher.

Retrieves the field-level schema for a single Data Lake Object from
``GET {instance_url}/services/data/v62.0/ssot/metadata/dlo/{name}`` and returns
a tuple of :class:`~models.FieldDef`. This is the per-DLO detail view (name,
type, keyQualifier) used to enrich the catalog produced by
:mod:`fetcher.metadata`.
"""

from __future__ import annotations

import time
from typing import Any, Final

import requests

from models import FieldDef

#: Salesforce Data API version used for the SSOT metadata endpoint.
API_VERSION: Final = "v62.0"
_MAX_ATTEMPTS: Final = 3
_BACKOFF_BASE_SECONDS: Final = 1.0


class StreamsError(RuntimeError):
    """Raised when a DLO schema cannot be retrieved."""


def fetch_dlo_schema(
    *,
    instance_url: str,
    access_token: str,
    dlo_name: str,
    timeout: float = 30.0,
) -> tuple[FieldDef, ...]:
    """Fetch the field schema for a single DLO.

    Retries transient transport errors and 5xx responses up to three times with
    exponential backoff (1s, 2s, 4s). The returned fields are sorted
    alphabetically for deterministic output.

    Args:
        instance_url: Base URL of the Salesforce org.
        access_token: OAuth bearer token.
        dlo_name: API name of the DLO (e.g. ``Order_Home__dll``).
        timeout: Per-request timeout in seconds.

    Returns:
        A tuple of :class:`~models.FieldDef`, sorted by field name.

    Raises:
        StreamsError: On a 4xx response or after exhausting retries.
    """
    base = instance_url.rstrip("/")
    url = f"{base}/services/data/{API_VERSION}/ssot/metadata/dlo/{dlo_name}"
    headers = {"Authorization": f"Bearer {access_token}"}

    last_error: str | None = None
    for attempt in range(_MAX_ATTEMPTS):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
        except requests.RequestException as exc:
            last_error = str(exc)
        else:
            if response.status_code == 200:
                return _parse_schema(response.json())
            if 400 <= response.status_code < 500:
                raise StreamsError(
                    f"DLO schema request rejected for {dlo_name!r} "
                    f"({response.status_code}): {response.text}"
                )
            last_error = f"HTTP {response.status_code}: {response.text}"
        if attempt < _MAX_ATTEMPTS - 1:
            time.sleep(_BACKOFF_BASE_SECONDS * (2**attempt))

    raise StreamsError(
        f"DLO schema request for {dlo_name!r} failed after "
        f"{_MAX_ATTEMPTS} attempts: {last_error}"
    )


def _parse_schema(payload: dict[str, Any]) -> tuple[FieldDef, ...]:
    """Normalize a raw DLO-schema response into sorted :class:`FieldDef`s."""
    fields = (FieldDef.from_api(f) for f in payload.get("fields", []))
    return tuple(sorted(fields, key=lambda fd: fd.name.lower()))
