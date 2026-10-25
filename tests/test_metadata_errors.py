"""Error-funnel regression tests for the metadata orchestrator.

Kept separate from test_metadata.py (which targets the pre-rewrite API and is
rewritten in Task 5). This file only locks in the Task 2 behavior: any
streams/fetch failure surfaces as MetadataError, never a leaked StreamsError.
"""

from __future__ import annotations

import pytest
import responses

from data360_autodoc.fetcher import metadata
from data360_autodoc.fetcher.streams import StreamsError

INSTANCE_URL = "https://example.my.salesforce.com"
API = "v62.0"
DMO_URL = f"{INSTANCE_URL}/services/data/{API}/ssot/data-model-objects"
STREAMS_URL = f"{INSTANCE_URL}/services/data/{API}/ssot/data-streams"


@responses.activate
def test_streams_failure_surfaces_as_metadata_error() -> None:
    # DMO list succeeds (empty -> no mapping calls); data-streams 404s.
    responses.add(responses.GET, DMO_URL, json={"dataModelObject": []}, status=200)
    responses.add(responses.GET, STREAMS_URL, status=404)

    # The 404 raises StreamsError inside fetch_dlos; fetch_metadata must funnel
    # it into MetadataError rather than letting StreamsError leak.
    with pytest.raises(metadata.MetadataError):
        metadata.fetch_metadata(
            instance_url=INSTANCE_URL, access_token="TOK", api_version=API
        )


def test_streams_error_is_not_a_metadata_error() -> None:
    # Guards the test above: if StreamsError were a MetadataError subclass,
    # pytest.raises(MetadataError) would pass without any funneling.
    assert not issubclass(StreamsError, metadata.MetadataError)


VERSIONS_URL = f"{INSTANCE_URL}/services/data/"


@responses.activate
def test_401_in_version_detection_is_not_hidden_by_the_fallback() -> None:
    responses.add(responses.GET, VERSIONS_URL, status=401)
    with pytest.raises(metadata.MetadataUnauthorized):
        metadata.fetch_metadata(instance_url=INSTANCE_URL, access_token="TOK")


@responses.activate
def test_401_on_one_dmo_aborts_the_run_instead_of_skipping() -> None:
    # CRITICAL regression: an expired token must not produce empty docs.
    responses.add(
        responses.GET,
        DMO_URL,
        json={
            "dataModelObject": [
                {"name": "A__dmo", "isEnabled": True},
                {"name": "B__dmo", "isEnabled": True},
            ]
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{INSTANCE_URL}/services/data/{API}/ssot/data-model-object-mappings",
        status=401,
    )
    with pytest.raises(metadata.MetadataUnauthorized):
        metadata.fetch_metadata(
            instance_url=INSTANCE_URL, access_token="TOK", api_version=API
        )


@responses.activate
def test_401_on_streams_is_unauthorized_not_a_generic_error() -> None:
    responses.add(responses.GET, DMO_URL, json={"dataModelObject": []}, status=200)
    responses.add(responses.GET, STREAMS_URL, status=401)
    with pytest.raises(metadata.MetadataUnauthorized):
        metadata.fetch_metadata(
            instance_url=INSTANCE_URL, access_token="TOK", api_version=API
        )


@responses.activate
def test_list_phase_reports_progress() -> None:
    responses.add(
        responses.GET,
        DMO_URL,
        json={"dataModelObject": [{"name": "Off__dmo", "isEnabled": False}]},
        status=200,
    )
    responses.add(responses.GET, STREAMS_URL, json={"dataStreams": []}, status=200)
    lines: list[str] = []
    metadata.fetch_metadata(
        instance_url=INSTANCE_URL,
        access_token="TOK",
        api_version=API,
        progress=lambda message, inline: lines.append(message),
    )
    assert "  Listing DMOs… 1 scanned" in lines
    assert "Fetching data streams…" in lines


def _one_good_one_broken_dmo() -> None:
    responses.add(
        responses.GET,
        DMO_URL,
        json={
            "dataModelObject": [
                {"name": "Good__dmo", "isEnabled": True},
                {"name": "Broken__dmo", "isEnabled": True},
            ]
        },
        status=200,
    )
    maps = f"{INSTANCE_URL}/services/data/{API}/ssot/data-model-object-mappings"
    responses.add(
        responses.GET,
        maps,
        json={"objectSourceTargetMaps": []},
        match=[
            responses.matchers.query_param_matcher(
                {"dataspace": "default", "dmoDeveloperName": "Good__dmo"}
            )
        ],
    )
    responses.add(
        responses.GET,
        maps,
        status=400,
        match=[
            responses.matchers.query_param_matcher(
                {"dataspace": "default", "dmoDeveloperName": "Broken__dmo"}
            )
        ],
    )
    responses.add(
        responses.GET,
        f"{DMO_URL}/Good__dmo/relationships",
        json={"relationships": []},
        status=200,
    )
    responses.add(responses.GET, STREAMS_URL, json={"dataStreams": []}, status=200)


@responses.activate
def test_partial_schema_is_returned_by_default() -> None:
    _one_good_one_broken_dmo()
    schema = metadata.fetch_metadata(
        instance_url=INSTANCE_URL, access_token="TOK", api_version=API
    )
    assert [d.name for d in schema.dmos] == ["Good__dmo"]


@responses.activate
def test_strict_refuses_a_partial_schema() -> None:
    # In CI a partial snapshot would diff as "Broken__dmo removed": false drift.
    _one_good_one_broken_dmo()
    with pytest.raises(metadata.MetadataError) as exc:
        metadata.fetch_metadata(
            instance_url=INSTANCE_URL, access_token="TOK", api_version=API, strict=True
        )
    assert "1 of 2 DMO(s) could not be read" in str(exc.value)
    assert "Broken__dmo" not in str(exc.value)  # names only in --verbose detail
    assert "Broken__dmo" in exc.value.detail
