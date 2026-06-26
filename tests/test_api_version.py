"""Tests for API-version autodetect + override (Task 3).

Kept separate from test_metadata.py (rewritten in Task 5). Covers the three
behaviors: default = autodetect highest, --api-version override, and the
fallback floor when discovery fails.
"""

from __future__ import annotations

import responses

from data360_autodoc.fetcher import metadata

INSTANCE_URL = "https://example.my.salesforce.com"
SERVICES_URL = f"{INSTANCE_URL}/services/data/"


def _versions(*nums: str) -> list[dict]:
    return [{"version": n, "url": f"/services/data/v{n}"} for n in nums]


# --- detect_api_version ------------------------------------------------------


@responses.activate
def test_detect_picks_highest_version() -> None:
    responses.add(
        responses.GET, SERVICES_URL, json=_versions("58.0", "62.0", "66.0"), status=200
    )
    got = metadata.detect_api_version(instance_url=INSTANCE_URL, access_token="TOK")
    assert got == "v66.0"


@responses.activate
def test_detect_falls_back_on_error() -> None:
    responses.add(responses.GET, SERVICES_URL, status=500)
    got = metadata.detect_api_version(
        instance_url=INSTANCE_URL, access_token="TOK", fallback="v62.0"
    )
    assert got == "v62.0"


@responses.activate
def test_detect_falls_back_on_empty_list() -> None:
    responses.add(responses.GET, SERVICES_URL, json=[], status=200)
    got = metadata.detect_api_version(
        instance_url=INSTANCE_URL, access_token="TOK", fallback="v62.0"
    )
    assert got == "v62.0"


# --- fetch_metadata threading ------------------------------------------------


def _stub_empty_org(version: str) -> None:
    base = f"{INSTANCE_URL}/services/data/{version}/ssot"
    responses.add(
        responses.GET,
        f"{base}/data-model-objects",
        json={"dataModelObject": []},
        status=200,
    )
    responses.add(
        responses.GET, f"{base}/data-streams", json={"dataStreams": []}, status=200
    )


@responses.activate
def test_explicit_version_skips_detection() -> None:
    _stub_empty_org("v66.0")
    metadata.fetch_metadata(
        instance_url=INSTANCE_URL, access_token="TOK", api_version="v66.0"
    )
    called = [c.request.url for c in responses.calls]
    assert SERVICES_URL not in called  # no autodetect
    assert any("v66.0/ssot/data-model-objects" in u for u in called)


@responses.activate
def test_none_version_autodetects_and_threads() -> None:
    responses.add(
        responses.GET, SERVICES_URL, json=_versions("62.0", "66.0"), status=200
    )
    _stub_empty_org("v66.0")
    metadata.fetch_metadata(
        instance_url=INSTANCE_URL, access_token="TOK", api_version=None
    )
    called = [c.request.url for c in responses.calls]
    assert SERVICES_URL in called  # detection ran
    # Detected v66.0 threaded into the subsequent fetch URLs.
    assert any("v66.0/ssot/data-model-objects" in u for u in called)
