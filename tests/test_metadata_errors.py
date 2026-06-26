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
