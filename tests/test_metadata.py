"""Tests for the Data 360 metadata orchestrator (real /ssot/* endpoints).

Covers the happy-path assembly across all four endpoints, DMO-list pagination +
deterministic sorting, and bearer auth. Edge behaviors live in focused files:
errors (test_metadata_errors), version detect/override (test_api_version), DMO
field enrichment (test_dmo_enrichment), partial-failure resilience
(test_dmo_resilience).
"""

from __future__ import annotations

import logging

import responses

from fetcher import metadata
from models import Mapping

INSTANCE_URL = "https://example.my.salesforce.com"
API = "v62.0"
SSOT = f"{INSTANCE_URL}/services/data/{API}/ssot"


def _fetch() -> object:
    return metadata.fetch_metadata(
        instance_url=INSTANCE_URL, access_token="TOK", api_version=API
    )


@responses.activate
def test_happy_path_assembles_full_org() -> None:
    # DMOs (one enabled, one disabled -> filtered out).
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json={
            "dataModelObject": [
                {"name": "Individual__dmo", "label": "Individual", "isEnabled": True},
                {"name": "Legacy__dmo", "label": "Legacy", "isEnabled": False},
            ]
        },
        status=200,
    )
    # Mappings: one DLO->DMO mapping + a mapping-only target field.
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-object-mappings",
        json={
            "objectSourceTargetMaps": [
                {
                    "sourceEntityDeveloperName": "Order_Home__dll",
                    "targetEntityDeveloperName": "Individual__dmo",
                    "fieldMappings": [{"targetFieldDeveloperName": "Email__c"}],
                }
            ]
        },
        status=200,
    )
    # Relationships: real field types (Email__c type beats mapping 'Unknown').
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects/Individual__dmo/relationships",
        json={
            "relationships": [
                {"status": "ACTIVE", "sourceField": {"name": "Id__c", "type": "Text"}},
                {
                    "status": "ACTIVE",
                    "sourceField": {"name": "Email__c", "type": "EmailAddress"},
                },
            ]
        },
        status=200,
    )
    # DLOs come from the data streams' dataLakeObjectInfo.
    responses.add(
        responses.GET,
        f"{SSOT}/data-streams",
        json={
            "dataStreams": [
                {
                    "dataLakeObjectInfo": {
                        "name": "Order_Home__dll",
                        "label": "Order (Home)",
                        "dataLakeFieldInfoRepresentation": [
                            {
                                "name": "OrderId",
                                "dataType": "Text",
                                "isPrimaryKey": True,
                            },
                            {"name": "Amount", "dataType": "Number"},
                        ],
                    }
                }
            ]
        },
        status=200,
    )

    schema = _fetch()

    # Org name resolved from the instance host.
    assert schema.org_name == "example.my.salesforce.com"

    # DMOs: disabled one filtered; relationship types win; fields sorted.
    (dmo,) = schema.dmos
    assert dmo.name == "Individual__dmo"
    assert [(f.name, f.type) for f in dmo.fields] == [
        ("Email__c", "EmailAddress"),
        ("Id__c", "Text"),
    ]

    # DLO assembled from the stream, with primary-key handling; fields sorted.
    (dlo,) = schema.dlos
    assert dlo.name == "Order_Home__dll"
    assert dlo.label == "Order (Home)"
    order_id = {f.name: f for f in dlo.fields}["OrderId"]
    assert order_id.is_key is True
    assert order_id.key_qualifier == "PrimaryKey"
    assert [f.name for f in dlo.fields] == ["Amount", "OrderId"]

    # DLO -> DMO mapping captured.
    assert schema.mappings == (
        Mapping(source_dlo="Order_Home__dll", target_dmo="Individual__dmo"),
    )


@responses.activate
def test_dmo_field_mappings_sheet3() -> None:
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json={
            "dataModelObject": [
                {"name": "ssot__Account__dlm", "label": "Account", "isEnabled": True}
            ]
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-object-mappings",
        json={
            "objectSourceTargetMaps": [
                {
                    "sourceEntityDeveloperName": "Account_CRM__dll",
                    "sourceEntityLabel": "Account_CRM",
                    "targetEntityDeveloperName": "ssot__Account__dlm",
                    "fieldMappings": [
                        {
                            "sourceFieldDeveloperName": "Id_c",
                            "targetFieldDeveloperName": "ssot__Id__c",
                        },
                        {
                            "sourceFieldDeveloperName": "Name_c",
                            "targetFieldDeveloperName": "ssot__Name__c",
                        },
                        {
                            "sourceFieldDeveloperName": "CreatedDate_c",
                            "targetFieldDeveloperName": "ssot__CreatedDate__c",
                        },
                    ],
                },
                {
                    # Blank sourceEntityLabel -> falls back to the DLO API name.
                    "sourceEntityDeveloperName": "Other__dll",
                    "sourceEntityLabel": "",
                    "targetEntityDeveloperName": "ssot__Account__dlm",
                    "fieldMappings": [
                        {
                            "sourceFieldDeveloperName": "Foo_c",
                            "targetFieldDeveloperName": "ssot__Foo__c",
                        }
                    ],
                },
            ]
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects/ssot__Account__dlm/relationships",
        json={"relationships": []},
        status=200,
    )
    responses.add(
        responses.GET, f"{SSOT}/data-streams", json={"dataStreams": []}, status=200
    )

    schema = _fetch()
    rows = schema.dmo_field_mappings
    assert len(rows) == 4  # 3 + 1 field mappings
    by = {(r.source_dlo_name, r.source_field_name): r for r in rows}

    r = by[("Account_CRM__dll", "Id_c")]
    assert r.source_dlo_label == "Account_CRM"
    assert r.target_dmo_name == "ssot__Account__dlm"
    assert r.target_dmo_label == "Account"  # from the queried DMO's label
    assert r.target_field_name == "ssot__Id__c"
    # No Describe in Python -> field labels fall back to API names.
    assert r.source_field_label == "Id_c"
    assert r.target_field_label == "ssot__Id__c"

    # Blank sourceEntityLabel falls back to the source DLO API name.
    assert by[("Other__dll", "Foo_c")].source_dlo_label == "Other__dll"


# Verified relationship shape captured from a live org (v67.0).
_REAL_REL = {
    "cardinality": "ManyToOne",
    "status": "INACTIVE",
    "name": "Account_PrimarySalesContactPointId_map_ContactPointEmail_Id_N_1_1",
    "sourceField": {
        "label": "Primary Sales Contact Point",
        "name": "ssot__PrimarySalesContactPointId__c",
        "type": "MktDataModelField",
    },
    "sourceObject": {
        "keyQualifierField": None,
        "label": "Account",
        "name": "ssot__Account__dlm",
    },
    "targetField": {
        "label": "Contact Point Email Id",
        "name": "ssot__Id__c",
        "type": "MktDataModelField",
    },
    "targetObject": {
        "keyQualifierField": None,
        "label": "Contact Point Email",
        "name": "ssot__ContactPointEmail__dlm",
    },
}


def test_parse_relationship_real_payload_target_side() -> None:
    # Queried DMO is the TARGET (Account points to ContactPointEmail).
    field, r = metadata._parse_relationship(_REAL_REL, "ssot__ContactPointEmail__dlm")
    # The queried DMO's own field is taken from targetField, not sourceField.
    assert field is not None and field.name == "ssot__Id__c"
    assert r is not None
    assert r.source_dmo_name == "ssot__Account__dlm"
    assert r.source_dmo_label == "Account"
    assert r.source_field == "ssot__PrimarySalesContactPointId__c"
    assert r.related_entity == "ssot__ContactPointEmail__dlm"
    assert r.related_field == "ssot__Id__c"
    assert r.cardinality == "N:1"  # "ManyToOne" normalized
    assert r.status == "INACTIVE"


def test_parse_relationship_real_payload_source_side() -> None:
    # Same payload, querying the SOURCE DMO -> field comes from sourceField.
    field, _ = metadata._parse_relationship(_REAL_REL, "ssot__Account__dlm")
    assert field is not None and field.name == "ssot__PrimarySalesContactPointId__c"


def test_parse_relationship_cardinality_variants() -> None:
    def card(value: str) -> str | None:
        _, r = metadata._parse_relationship(
            {
                "sourceObject": {"name": "A"},
                "targetObject": {"name": "B"},
                "cardinality": value,
            },
            "A",
        )
        assert r is not None
        return r.cardinality

    assert card("OneToOne") == "1:1"
    assert card("OneToMany") == "1:N"
    assert card("ManyToMany") == "N:N"


def test_parse_relationship_flattened_fallback() -> None:
    # Defensive fallback for any org/version that flattens the nested objects.
    rel = {
        "sourceEntityDeveloperName": "ssot__Account__dlm",
        "sourceFieldDeveloperName": "PartyId",
        "targetEntityDeveloperName": "ssot__Individual__dlm",
        "targetFieldDeveloperName": "Id",
        "cardinality": "ManyToOne",
    }
    field, r = metadata._parse_relationship(rel, "ssot__Account__dlm")
    assert field is None  # no nested field dict -> no FieldDef
    assert r is not None
    assert r.source_dmo_name == "ssot__Account__dlm"
    assert r.related_entity == "ssot__Individual__dlm"
    assert r.related_field == "Id"
    assert r.cardinality == "N:1"


def test_parse_relationship_empty_returns_none() -> None:
    field, r = metadata._parse_relationship({"status": "ACTIVE"}, "D__dlm")
    assert field is None
    assert r is None  # no relationship info at all -> row dropped (not blank-spammed)


@responses.activate
def test_relationships_labels_and_dlo_type_inference() -> None:
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json={
            "dataModelObject": [
                {"name": "ssot__Account__dlm", "label": "Account", "isEnabled": True}
            ]
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-object-mappings",
        json={
            "objectSourceTargetMaps": [
                {
                    "sourceEntityDeveloperName": "Account_CRM__dll",
                    "sourceEntityLabel": "",  # blank -> enrich from stream label
                    "targetEntityDeveloperName": "ssot__Account__dlm",
                    "fieldMappings": [
                        {  # no payload label -> enrich from DLO field label
                            "sourceFieldDeveloperName": "Id__c",
                            "targetFieldDeveloperName": "ssot__Id__c",
                        },
                        {
                            "sourceFieldDeveloperName": "AnnualRevenue__c",
                            "targetFieldDeveloperName": "ssot__Revenue__c",
                        },
                    ],
                }
            ]
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects/ssot__Account__dlm/relationships",
        json={
            "relationships": [
                {
                    "status": "ACTIVE",
                    "cardinality": "ManyToOne",
                    "name": "AccountToIndividual",
                    "sourceObject": {"name": "ssot__Account__dlm", "label": "Account"},
                    "sourceField": {"name": "ssot__PartyId__c", "type": "Text"},
                    "targetObject": {
                        "name": "ssot__Individual__dlm",
                        "label": "Individual",
                    },
                    "targetField": {
                        "name": "ssot__Id__c",
                        "type": "MktDataModelField",
                    },
                }
            ]
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-streams",
        json={
            "dataStreams": [
                {
                    "name": "Account_CRM",
                    "connectorInfo": {"connectorType": "SalesforceDotCom"},
                    "dataLakeObjectInfo": {
                        "name": "Account_CRM__dll",
                        "label": "Account_CRM",
                        "dataLakeFieldInfoRepresentation": [
                            {
                                "name": "Id",
                                "label": "Account ID",
                                "dataType": "Text",
                                "isPrimaryKey": True,
                            },
                            {
                                "name": "AnnualRevenue",
                                "label": "Annual Revenue",
                                "dataType": "Number",
                            },
                        ],
                    },
                }
            ]
        },
        status=200,
    )

    schema = _fetch()

    # 1) Relationships are preserved (not discarded).
    (rel,) = schema.relationships
    assert rel.source_dmo_name == "ssot__Account__dlm"
    assert rel.source_field == "ssot__PartyId__c"
    assert rel.related_entity == "ssot__Individual__dlm"
    assert rel.related_field == "ssot__Id__c"
    assert rel.cardinality == "N:1"  # MANYTOONE normalized
    assert rel.relationship_label == "AccountToIndividual"

    # 2) DLO→DMO labels enriched from DLO metadata (not API-name fallback).
    by = {r.source_field_name: r for r in schema.dmo_field_mappings}
    assert by["Id__c"].source_field_label == "Account ID"
    assert by["Id__c"].source_dlo_label == "Account_CRM"

    # 3) Generic DMO field types resolved from the mapped DLO field type.
    #    The type token stays clean; provenance lives in type_inferred.
    (dmo,) = schema.dmos
    by_field = {f.name: f for f in dmo.fields}
    assert by_field["ssot__Id__c"].type == "Text"
    assert by_field["ssot__Id__c"].type_inferred is True
    assert by_field["ssot__Revenue__c"].type == "Number"
    assert by_field["ssot__Revenue__c"].type_inferred is True
    # A concrete type from the relationships endpoint is left untouched.
    assert by_field["ssot__PartyId__c"].type == "Text"
    assert by_field["ssot__PartyId__c"].type_inferred is False


@responses.activate
def test_dmo_list_pagination_and_sorting() -> None:
    # Two pages of DMOs; Zeta arrives first, Alpha second.
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json={
            "dataModelObject": [
                {"name": "Zeta__dmo", "label": "Zeta", "isEnabled": True}
            ],
            "nextPageUrl": f"/services/data/{API}/ssot/data-model-objects?page=2",
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json={
            "dataModelObject": [
                {"name": "Alpha__dmo", "label": "Alpha", "isEnabled": True}
            ]
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-object-mappings",
        json={"objectSourceTargetMaps": []},
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects/Zeta__dmo/relationships",
        json={"relationships": []},
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects/Alpha__dmo/relationships",
        json={"relationships": []},
        status=200,
    )
    responses.add(
        responses.GET, f"{SSOT}/data-streams", json={"dataStreams": []}, status=200
    )

    schema = _fetch()

    # Both pages fetched; output sorted alphabetically (deterministic).
    assert [d.name for d in schema.dmos] == ["Alpha__dmo", "Zeta__dmo"]


@responses.activate
def test_bearer_header_sent() -> None:
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json={"dataModelObject": []},
        status=200,
    )
    responses.add(
        responses.GET, f"{SSOT}/data-streams", json={"dataStreams": []}, status=200
    )

    _fetch()

    assert responses.calls[0].request.headers["Authorization"] == "Bearer TOK"


@responses.activate
def test_dmo_list_caps_and_warns(caplog) -> None:
    # One more enabled DMO than the cap -> truncated to _MAX_DMOS, with a warning.
    over = metadata._MAX_DMOS + 1
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json={
            "dataModelObject": [
                {"name": f"D{i}__dmo", "label": f"D{i}", "isEnabled": True}
                for i in range(over)
            ]
        },
        status=200,
    )

    with caplog.at_level(logging.WARNING):
        out = metadata._fetch_dmo_list(INSTANCE_URL, API, "TOK", 5.0)

    assert len(out) == metadata._MAX_DMOS
    assert "DMO list capped at" in caplog.text


@responses.activate
def test_progress_callback_is_invoked() -> None:
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects",
        json={"dataModelObject": [{"name": "A__dmo", "label": "A", "isEnabled": True}]},
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-object-mappings",
        json={"objectSourceTargetMaps": []},
        status=200,
    )
    responses.add(
        responses.GET,
        f"{SSOT}/data-model-objects/A__dmo/relationships",
        json={"relationships": []},
        status=200,
    )
    responses.add(
        responses.GET, f"{SSOT}/data-streams", json={"dataStreams": []}, status=200
    )

    events: list[tuple[str, bool]] = []
    metadata.fetch_metadata(
        instance_url=INSTANCE_URL,
        access_token="TOK",
        api_version=API,
        progress=lambda msg, inline: events.append((msg, inline)),
    )

    msgs = [m for m, _ in events]
    assert any("1/1" in m for m in msgs)  # per-DMO inline counter
    assert any("data streams" in m.lower() for m in msgs)  # phase line
    assert any(inline for _, inline in events)  # at least one in-place update
