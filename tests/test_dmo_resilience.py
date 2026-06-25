"""Task 4B: per-DMO partial-failure resilience.

One DMO failing (mappings OR relationships) must be skipped with a warning, not
sink the whole document. Kept out of test_metadata.py (rewritten in Task 5).
"""

from __future__ import annotations

import logging

import responses

from fetcher import metadata

INSTANCE_URL = "https://example.my.salesforce.com"
API = "v62.0"
SSOT = f"{INSTANCE_URL}/services/data/{API}/ssot"


def _dmo_list(*names: str) -> dict:
    return {
        "dataModelObject": [{"name": n, "label": n, "isEnabled": True} for n in names]
    }


@responses.activate
def test_relationships_failure_skips_one_dmo(caplog) -> None:
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json=_dmo_list("Good__dmo", "Bad__dmo"),
        status=200,
    )
    # Mappings: one registration serves both DMOs (query ignored), empty.
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-object-mappings",
        json={"objectSourceTargetMaps": []},
        status=200,
    )
    # Good DMO relationships OK; Bad DMO relationships 404 -> skip.
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects/Good__dmo/relationships",
        json={
            "relationships": [
                {"status": "ACTIVE", "sourceField": {"name": "Id__c", "type": "Text"}}
            ]
        },
        status=200,
    )
    responses.add(
        responses.GET, f"{SSOT}/data-model-objects/Bad__dmo/relationships", status=404
    )
    responses.add(
        responses.GET, f"{SSOT}/data-streams", json={"dataStreams": []}, status=200
    )

    with caplog.at_level(logging.WARNING):
        schema = metadata.fetch_metadata(
            instance_url=INSTANCE_URL, access_token="TOK", api_version=API
        )

    # Bad DMO dropped; Good survives with its enriched field.
    assert [d.name for d in schema.dmos] == ["Good__dmo"]
    assert schema.dmos[0].fields[0].name == "Id__c"
    # Per-DMO warning + summary warning.
    assert "Skipping DMO Bad__dmo" in caplog.text
    assert "Skipped 1 of 2" in caplog.text


@responses.activate
def test_mappings_failure_skips_one_dmo(caplog) -> None:
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json=_dmo_list("Lone__dmo"),
        status=200,
    )
    # Mappings call (made before relationships) 404s -> DMO skipped.
    responses.add(responses.GET, f"{SSOT}/data-model-object-mappings", status=404)
    responses.add(
        responses.GET, f"{SSOT}/data-streams", json={"dataStreams": []}, status=200
    )

    with caplog.at_level(logging.WARNING):
        schema = metadata.fetch_metadata(
            instance_url=INSTANCE_URL, access_token="TOK", api_version=API
        )

    # The only DMO was skipped; doc still builds (no exception).
    assert schema.dmos == ()
    assert "Skipping DMO Lone__dmo" in caplog.text
