"""Task 4A: DMO field enrichment from the relationships endpoint.

Verifies that DMO fields get real types from /ssot/.../relationships, that
relationship types win over mapping-derived 'Unknown', that mapping-only fields
are still kept, and that inactive relationships are skipped. Kept out of
test_metadata.py (rewritten in Task 5).
"""

from __future__ import annotations

import responses

from data360_autodoc.fetcher import metadata

INSTANCE_URL = "https://example.my.salesforce.com"
API = "v62.0"
SSOT = f"{INSTANCE_URL}/services/data/{API}/ssot"
DMO = "Individual__dmo"


@responses.activate
def test_dmo_fields_enriched_from_relationships() -> None:
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json={
            "dataModelObject": [{"name": DMO, "label": "Individual", "isEnabled": True}]
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-object-mappings",
        json={
            "objectSourceTargetMaps": [
                {
                    "sourceEntityDeveloperName": "Order_Home__dll",
                    "targetEntityDeveloperName": DMO,
                    "fieldMappings": [
                        {"targetFieldDeveloperName": "MappedOnly__c"},
                        {"targetFieldDeveloperName": "Shared__c"},
                    ],
                }
            ]
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects/{DMO}/relationships",
        json={
            "relationships": [
                {"status": "ACTIVE", "sourceField": {"name": "Id__c", "type": "Text"}},
                {
                    "status": "ACTIVE",
                    "sourceField": {"name": "Shared__c", "type": "Number"},
                },
                {
                    "status": "INACTIVE",
                    "sourceField": {"name": "Skip__c", "type": "Text"},
                },
            ]
        },
        status=200,
    )
    responses.add(
        responses.GET, f"{SSOT}/data-streams", json={"dataStreams": []}, status=200
    )

    schema = metadata.fetch_metadata(
        instance_url=INSTANCE_URL, access_token="TOK", api_version=API
    )

    (dmo,) = schema.dmos
    by_name = {f.name: f.type for f in dmo.fields}

    # Real type from relationships (was 'Unknown' before Task 4A).
    assert by_name["Id__c"] == "Text"
    # Relationship type wins over the mapping-derived 'Unknown'.
    assert by_name["Shared__c"] == "Number"
    # Mapping-only field is still kept, with 'Unknown' (no relationship for it).
    assert by_name["MappedOnly__c"] == "Unknown"
    # Inactive relationship is skipped.
    assert "Skip__c" not in by_name
    # Deterministic alphabetical field order.
    assert [f.name for f in dmo.fields] == ["Id__c", "MappedOnly__c", "Shared__c"]
