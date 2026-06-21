"""Data 360 metadata fetcher.

Pulls the org-wide metadata catalog (DMOs, DLOs, CIOs, identity rulesets and
DLO→DMO mappings) from ``GET {instance_url}/api/v1/metadata/`` and normalizes it
into an :class:`~models.OrgSchema`.

The endpoint is assumed to be page-based: each response carries a ``page`` of
entities plus a ``totalSize`` and an optional ``nextPageUrl``. We follow
``nextPageUrl`` until exhausted so orgs with more than 1000 entities are fully
captured. See ``agent_docs/api_reference.md`` for the assumed payload shape.
"""

from __future__ import annotations

import time
from typing import Any, Final

import requests

from models import OrgSchema

#: Entity collection keys merged across pages.
_COLLECTION_KEYS: Final = (
    "dmos",
    "dlos",
    "cios",
    "identityResolutionRulesets",
    "mappings",
)
_MAX_ATTEMPTS: Final = 3
_BACKOFF_BASE_SECONDS: Final = 1.0


class MetadataError(RuntimeError):
    """Raised when the metadata catalog cannot be retrieved."""


def _get_with_retry(url: str, *, access_token: str, timeout: float) -> dict[str, Any]:
    """GET ``url`` with bearer auth, retrying transient failures.

    Args:
        url: Absolute URL to request.
        access_token: OAuth bearer token.
        timeout: Per-request timeout in seconds.

    Returns:
        The decoded JSON body.

    Raises:
        MetadataError: On a 4xx response or after exhausting retries.
    """
    headers = {"Authorization": f"Bearer {access_token}"}
    last_error: str | None = None
    for attempt in range(_MAX_ATTEMPTS):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
        except requests.RequestException as exc:
            last_error = str(exc)
        else:
            if response.status_code == 200:
                return response.json()
            if 400 <= response.status_code < 500:
                raise MetadataError(
                    f"Metadata request rejected ({response.status_code}): "
                    f"{response.text}"
                )
            last_error = f"HTTP {response.status_code}: {response.text}"
        if attempt < _MAX_ATTEMPTS - 1:
            time.sleep(_BACKOFF_BASE_SECONDS * (2**attempt))
    raise MetadataError(
        f"Metadata request failed after {_MAX_ATTEMPTS} attempts: {last_error}"
    )


def fetch_metadata(
    *,
    instance_url: str,
    access_token: str,
    org_name: str | None = None,
    timeout: float = 60.0,
) -> OrgSchema:
    """Fetch and normalize the full org metadata catalog.

    Transparently follows pagination (via each page's ``nextPageUrl``) so orgs
    with more than 1000 entities are captured completely, then merges all pages
    and hands the aggregate to :meth:`models.OrgSchema.from_metadata`.

    Args:
        instance_url: Base URL of the Salesforce org.
        access_token: OAuth bearer token from :func:`fetcher.auth.get_access_token`.
        org_name: Optional human-readable org name for the document title.
        timeout: Per-request timeout in seconds.

    Returns:
        A normalized :class:`~models.OrgSchema`.

    Raises:
        MetadataError: If any page request fails.
    """
    base = instance_url.rstrip("/")
    next_url: str | None = f"{base}/api/v1/metadata/"
    merged: dict[str, list[dict[str, Any]]] = {k: [] for k in _COLLECTION_KEYS}
    resolved_org_name = org_name
    seen_urls: set[str] = set()

    while next_url:
        if next_url in seen_urls:
            raise MetadataError(
                f"Pagination cycle detected: {next_url} was already fetched. "
                "The org returned a self-referential or repeating nextPageUrl."
            )
        seen_urls.add(next_url)
        page = _get_with_retry(next_url, access_token=access_token, timeout=timeout)
        for key in _COLLECTION_KEYS:
            merged[key].extend(page.get(key, []))
        if resolved_org_name is None:
            resolved_org_name = page.get("orgName")
        next_url = _resolve_next_url(page, base)

    payload: dict[str, Any] = dict(merged)
    if resolved_org_name is not None:
        payload["orgName"] = resolved_org_name
    return OrgSchema.from_metadata(
        payload, instance_url=instance_url, org_name=org_name
    )


def _resolve_next_url(page: dict[str, Any], base: str) -> str | None:
    """Return the absolute URL of the next page, or ``None`` if finished.

    Accepts either an absolute ``nextPageUrl`` or a relative path, normalizing
    the latter against ``base``.
    """
    nxt = page.get("nextPageUrl")
    if not nxt:
        return None
    if nxt.startswith("http://") or nxt.startswith("https://"):
        return nxt
    return f"{base}/{nxt.lstrip('/')}"
