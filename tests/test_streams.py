"""Unit tests for the DLO/stream fetcher (over /ssot/data-streams).

DLOs, per-stream rows, and field mappings are all extracted from each stream's
``dataLakeObjectInfo`` in a single pass via :func:`fetch_dlos_and_streams`; the
helpers below unpack the piece each test cares about. Integration with the rest
of the org schema is covered in test_metadata.py.
"""

from __future__ import annotations

import pytest
import responses

from data360_autodoc.fetcher.streams import StreamsError, fetch_dlos_and_streams

INSTANCE_URL = "https://example.my.salesforce.com"
API = "v62.0"
STREAMS_URL = f"{INSTANCE_URL}/services/data/{API}/ssot/data-streams"


def _stream(
    name: str, label: str | None = None, fields: list[dict] | None = None
) -> dict:
    return {
        "dataLakeObjectInfo": {
            "name": name,
            "label": label or name,
            "dataLakeFieldInfoRepresentation": fields or [],
        }
    }


def _fetch() -> tuple:
    """Return just the DLOs from the single-pass fetch."""
    dlos, _, _ = fetch_dlos_and_streams(
        instance_url=INSTANCE_URL, access_token="TOK", api_version=API
    )
    return dlos


@responses.activate
def test_happy_path_dlo_with_fields() -> None:
    responses.add(
        responses.GET,
        STREAMS_URL,
        json={
            "dataStreams": [
                _stream(
                    "Order_Home__dll",
                    "Order (Home)",
                    [
                        {"name": "OrderId", "dataType": "Text", "isPrimaryKey": True},
                        {"name": "Amount", "dataType": "Number"},
                    ],
                )
            ]
        },
        status=200,
    )
    (dlo,) = _fetch()
    assert dlo.name == "Order_Home__dll"
    assert dlo.label == "Order (Home)"
    # Fields sorted alphabetically.
    assert [f.name for f in dlo.fields] == ["Amount", "OrderId"]
    assert {f.name: f.type for f in dlo.fields} == {
        "Amount": "Number",
        "OrderId": "Text",
    }


@responses.activate
def test_primary_key_handling() -> None:
    responses.add(
        responses.GET,
        STREAMS_URL,
        json={
            "dataStreams": [
                _stream(
                    "D__dll",
                    fields=[
                        {"name": "Pk", "dataType": "Text", "isPrimaryKey": True},
                        {"name": "Plain", "dataType": "Text"},
                    ],
                )
            ]
        },
        status=200,
    )
    (dlo,) = _fetch()
    by = {f.name: f for f in dlo.fields}
    assert by["Pk"].is_key is True
    assert by["Pk"].key_qualifier == "PrimaryKey"
    assert by["Plain"].is_key is False
    assert by["Plain"].key_qualifier is None


@responses.activate
def test_dedup_dlo_across_streams() -> None:
    # Two streams reference the same DLO -> first occurrence wins.
    responses.add(
        responses.GET,
        STREAMS_URL,
        json={
            "dataStreams": [
                _stream(
                    "Order_Home__dll", fields=[{"name": "First", "dataType": "Text"}]
                ),
                _stream(
                    "Order_Home__dll", fields=[{"name": "Second", "dataType": "Text"}]
                ),
            ]
        },
        status=200,
    )
    dlos = _fetch()
    assert len(dlos) == 1
    assert [f.name for f in dlos[0].fields] == ["First"]


@responses.activate
def test_pagination_over_data_streams() -> None:
    responses.add(
        responses.GET,
        STREAMS_URL,
        json={
            "dataStreams": [_stream("A__dll")],
            "nextPageUrl": f"/services/data/{API}/ssot/data-streams?page=2",
        },
        status=200,
    )
    responses.add(
        responses.GET,
        STREAMS_URL,
        json={"dataStreams": [_stream("B__dll")]},
        status=200,
    )
    dlos = _fetch()
    assert {d.name for d in dlos} == {"A__dll", "B__dll"}


@responses.activate
def test_empty_streams_returns_empty() -> None:
    responses.add(responses.GET, STREAMS_URL, json={"dataStreams": []}, status=200)
    assert _fetch() == ()


@responses.activate
def test_streams_error_on_4xx() -> None:
    responses.add(responses.GET, STREAMS_URL, status=403)
    with pytest.raises(StreamsError):
        _fetch()


# --- DataStream metadata extraction ------------------------------------------


def _fetch_streams() -> tuple:
    """Return just the per-stream rows from the single-pass fetch."""
    _, streams, _ = fetch_dlos_and_streams(
        instance_url=INSTANCE_URL, access_token="TOK", api_version=API
    )
    return streams


@responses.activate
def test_data_stream_full_metadata() -> None:
    responses.add(
        responses.GET,
        STREAMS_URL,
        json={
            "dataStreams": [
                {
                    "name": "Account_CRM_Stream",
                    "connectorInfo": {"connectorName": "Salesforce CRM"},
                    "refreshConfig": {
                        "refreshMode": "UPSERT",
                        "frequency": {"frequencyType": "BATCH"},
                    },
                    "advancedAttributes": {
                        "dataExtensionExtractionMode": "INCREMENTAL",
                        "organizationUnitIdentifier": "OU-1",
                    },
                    "dataLakeObjectInfo": {
                        "name": "Account_CRM__dll",
                        "label": "Account_CRM",
                        "category": "Profile",
                        "eventDateTimeFieldName": "CreatedDate",
                        "dataLakeFieldInfoRepresentation": [
                            {"name": "Id", "dataType": "Text", "isPrimaryKey": True},
                            {
                                "name": "FullName",
                                "dataType": "Text",
                                "isFormula": True,
                                "formula": "First + Last",
                            },
                        ],
                    },
                }
            ]
        },
        status=200,
    )
    (s,) = _fetch_streams()
    assert s.name == "Account_CRM_Stream"
    assert s.dlo_name == "Account_CRM__dll"
    assert s.dlo_label == "Account_CRM"
    assert s.data_source == "Salesforce CRM"
    assert s.category == "Profile"
    assert s.event_time_field == "CreatedDate"
    assert s.primary_keys == ("Id",)
    assert s.formula_fields == ("FullName",)
    assert s.formula_calculations == ("First + Last",)
    assert s.org_unit_identifier == "OU-1"
    assert s.schedule_frequency == "BATCH"
    assert s.refresh_mode == "UPSERT"
    assert s.de_extraction_mode == "INCREMENTAL"


@responses.activate
def test_data_stream_missing_fields_are_none() -> None:
    responses.add(
        responses.GET,
        STREAMS_URL,
        json={
            "dataStreams": [
                {
                    "name": "Bare_Stream",
                    "dataLakeObjectInfo": {
                        "name": "Bare__dll",
                        "label": "Bare",
                        "dataLakeFieldInfoRepresentation": [],
                    },
                }
            ]
        },
        status=200,
    )
    (s,) = _fetch_streams()
    assert s.name == "Bare_Stream"
    assert s.dlo_name == "Bare__dll"
    assert s.data_source is None
    assert s.category is None
    assert s.event_time_field is None
    assert s.primary_keys == ()
    assert s.formula_fields == ()
    assert s.formula_calculations == ()
    assert s.org_unit_identifier is None
    assert s.schedule_frequency is None
    assert s.refresh_mode is None
    assert s.de_extraction_mode is None


@responses.activate
def test_dlos_and_streams_single_pass() -> None:
    responses.add(
        responses.GET,
        STREAMS_URL,
        json={
            "dataStreams": [
                {
                    "name": "S1",
                    "dataLakeObjectInfo": {
                        "name": "X__dll",
                        "label": "X",
                        "dataLakeFieldInfoRepresentation": [
                            {"name": "Id", "dataType": "Text", "isPrimaryKey": True}
                        ],
                    },
                }
            ]
        },
        status=200,
    )
    dlos, streams, field_mappings = fetch_dlos_and_streams(
        instance_url=INSTANCE_URL, access_token="TOK", api_version=API
    )
    assert [d.name for d in dlos] == ["X__dll"]
    assert [s.dlo_name for s in streams] == ["X__dll"]
    assert [fm.dlo_field_name for fm in field_mappings] == ["Id"]
    assert len(responses.calls) == 1  # single pass over /ssot/data-streams


@responses.activate
def test_field_mappings_extraction() -> None:
    responses.add(
        responses.GET,
        STREAMS_URL,
        json={
            "dataStreams": [
                {
                    "name": "Account_CRM",
                    "connectorInfo": {"connectorType": "SalesforceDotCom"},
                    "sourceFields": [
                        {"name": "SLASerialNumber__c"},
                        {"name": "Website"},
                    ],
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
                                "name": "KQ_Id",
                                "label": "KQ_Id",
                                "dataType": "Text",
                                "isPrimaryKey": False,
                            },
                            {
                                "name": "SLASerialNumber_c",
                                "label": "SLA Serial Number",
                                "dataType": "Text",
                                "isPrimaryKey": False,
                            },
                            {
                                "name": "Website",
                                "label": "Website",
                                "dataType": "Url",
                                "isPrimaryKey": False,
                            },
                        ],
                    },
                }
            ]
        },
        status=200,
    )
    _, _, fms = fetch_dlos_and_streams(
        instance_url=INSTANCE_URL, access_token="TOK", api_version=API
    )
    by = {fm.dlo_field_name: fm for fm in fms}

    # Mapped Data Stream + Data Source filled for every row.
    assert all(fm.stream_name == "Account_CRM" for fm in fms)
    assert all(fm.data_source == "SalesforceDotCom" for fm in fms)
    # Field Label DLO from field.label; Data Type from dataType.
    assert by["Id"].dlo_field_label == "Account ID"
    assert by["Website"].data_type == "Url"
    # Primary key.
    assert by["Id"].is_primary_key is True
    # Foreign key: KQ_ heuristic only.
    assert by["KQ_Id"].is_foreign_key is True
    assert by["Id"].is_foreign_key is False
    # Field Label Source reverse-mapped (__ -> _); system fields have no source.
    assert by["SLASerialNumber_c"].source_field == "SLASerialNumber__c"
    assert by["Website"].source_field == "Website"
    assert by["KQ_Id"].source_field is None
    # DLO API name carried on every row; nullable absent from this payload -> None.
    assert all(fm.dlo_name == "Account_CRM__dll" for fm in fms)
    assert all(fm.nullable is None for fm in fms)
