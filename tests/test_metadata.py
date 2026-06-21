"""Mock tests for the metadata catalog fetcher."""

from __future__ import annotations

import pytest
import responses

from fetcher import metadata

INSTANCE_URL = "https://example.my.salesforce.com"
META_URL = f"{INSTANCE_URL}/api/v1/metadata/"


def _page_one() -> dict:
    return {
        "orgName": "Acme Data Cloud",
        "totalSize": 2,
        "nextPageUrl": "/api/v1/metadata/?page=2",
        "dmos": [
            {
                "name": "Individual__dmo",
                "label": "Individual",
                "fields": [
                    {"name": "Id__c", "type": "Text", "isKey": True},
                    {"name": "FirstName__c", "type": "Text"},
                ],
            }
        ],
        "dlos": [
            {
                "name": "Order_Home__dll",
                "label": "Order (Home)",
                "fields": [{"name": "OrderId", "type": "Text", "isKey": True}],
            }
        ],
        "cios": [],
        "identityResolutionRulesets": [],
        "mappings": [{"sourceDlo": "Order_Home__dll", "targetDmo": "Individual__dmo"}],
    }


def _page_two() -> dict:
    return {
        "orgName": "Acme Data Cloud",
        "totalSize": 2,
        "nextPageUrl": None,
        "dmos": [{"name": "Account__dmo", "label": "Account", "fields": []}],
        "dlos": [],
        "cios": [
            {
                "name": "CLV__cio",
                "label": "Customer Lifetime Value",
                "dimensions": ["Individual__dmo.Id__c"],
                "measures": ["TotalSpend"],
            }
        ],
        "identityResolutionRulesets": [
            {
                "name": "Default_Ruleset",
                "label": "Default Ruleset",
                "matchRules": ["Exact Email"],
                "reconciliationRule": "Most Recent",
            }
        ],
        "mappings": [],
    }


@responses.activate
def test_fetch_metadata_single_page() -> None:
    page = _page_one()
    page["nextPageUrl"] = None
    responses.add(responses.GET, META_URL, json=page, status=200)

    schema = metadata.fetch_metadata(instance_url=INSTANCE_URL, access_token="TOK")

    assert schema.org_name == "Acme Data Cloud"
    assert [d.name for d in schema.dmos] == ["Individual__dmo"]
    assert schema.dmos[0].fields[0].name == "FirstName__c"  # sorted
    assert len(responses.calls) == 1


@responses.activate
def test_fetch_metadata_follows_pagination() -> None:
    responses.add(responses.GET, META_URL, json=_page_one(), status=200)
    responses.add(
        responses.GET,
        f"{INSTANCE_URL}/api/v1/metadata/?page=2",
        json=_page_two(),
        status=200,
    )

    schema = metadata.fetch_metadata(instance_url=INSTANCE_URL, access_token="TOK")

    # DMOs from both pages, alphabetically sorted.
    assert [d.name for d in schema.dmos] == ["Account__dmo", "Individual__dmo"]
    assert [c.name for c in schema.cios] == ["CLV__cio"]
    assert [r.name for r in schema.identity_rulesets] == ["Default_Ruleset"]
    assert schema.mappings[0].source_dlo == "Order_Home__dll"
    assert len(responses.calls) == 2


@responses.activate
def test_fetch_metadata_bearer_header_sent() -> None:
    page = _page_one()
    page["nextPageUrl"] = None
    responses.add(responses.GET, META_URL, json=page, status=200)

    metadata.fetch_metadata(instance_url=INSTANCE_URL, access_token="TOK")

    assert responses.calls[0].request.headers["Authorization"] == "Bearer TOK"


@responses.activate
def test_fetch_metadata_retries_then_succeeds() -> None:
    page = _page_one()
    page["nextPageUrl"] = None
    responses.add(responses.GET, META_URL, status=500)
    responses.add(responses.GET, META_URL, json=page, status=200)

    schema = metadata.fetch_metadata(instance_url=INSTANCE_URL, access_token="TOK")

    assert schema.org_name == "Acme Data Cloud"
    assert len(responses.calls) == 2


@responses.activate
def test_fetch_metadata_4xx_raises() -> None:
    responses.add(responses.GET, META_URL, status=403)
    with pytest.raises(metadata.MetadataError):
        metadata.fetch_metadata(instance_url=INSTANCE_URL, access_token="TOK")
    assert len(responses.calls) == 1


@responses.activate
def test_fetch_metadata_detects_pagination_cycle() -> None:
    # Page points back at the first metadata URL -> would loop forever.
    cyclic = _page_one()
    cyclic["nextPageUrl"] = "/api/v1/metadata/"
    responses.add(responses.GET, META_URL, json=cyclic, status=200)

    with pytest.raises(metadata.MetadataError, match="cycle"):
        metadata.fetch_metadata(instance_url=INSTANCE_URL, access_token="TOK")
