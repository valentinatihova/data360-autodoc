"""Mock tests for the DLO schema (Data Streams) fetcher."""

from __future__ import annotations

import pytest
import responses

from fetcher import streams

INSTANCE_URL = "https://example.my.salesforce.com"
DLO_NAME = "Order_Home__dll"
DLO_URL = (
    f"{INSTANCE_URL}/services/data/{streams.API_VERSION}"
    f"/ssot/metadata/dlo/{DLO_NAME}"
)


def _schema() -> dict:
    return {
        "name": DLO_NAME,
        "fields": [
            {"name": "OrderId", "type": "Text", "keyQualifier": "PrimaryKey"},
            {"name": "Amount", "type": "Number"},
        ],
    }


@responses.activate
def test_fetch_dlo_schema_success() -> None:
    responses.add(responses.GET, DLO_URL, json=_schema(), status=200)

    fields = streams.fetch_dlo_schema(
        instance_url=INSTANCE_URL, access_token="TOK", dlo_name=DLO_NAME
    )

    # Sorted alphabetically: Amount before OrderId.
    assert [f.name for f in fields] == ["Amount", "OrderId"]
    order_id = next(f for f in fields if f.name == "OrderId")
    assert order_id.is_key is True
    assert order_id.key_qualifier == "PrimaryKey"


@responses.activate
def test_fetch_dlo_schema_bearer_header_sent() -> None:
    responses.add(responses.GET, DLO_URL, json=_schema(), status=200)

    streams.fetch_dlo_schema(
        instance_url=INSTANCE_URL, access_token="TOK", dlo_name=DLO_NAME
    )

    assert responses.calls[0].request.headers["Authorization"] == "Bearer TOK"


@responses.activate
def test_fetch_dlo_schema_retries_then_succeeds() -> None:
    responses.add(responses.GET, DLO_URL, status=502)
    responses.add(responses.GET, DLO_URL, json=_schema(), status=200)

    fields = streams.fetch_dlo_schema(
        instance_url=INSTANCE_URL, access_token="TOK", dlo_name=DLO_NAME
    )

    assert len(fields) == 2
    assert len(responses.calls) == 2


@responses.activate
def test_fetch_dlo_schema_4xx_raises() -> None:
    responses.add(responses.GET, DLO_URL, status=404)
    with pytest.raises(streams.StreamsError):
        streams.fetch_dlo_schema(
            instance_url=INSTANCE_URL, access_token="TOK", dlo_name=DLO_NAME
        )
    assert len(responses.calls) == 1


@responses.activate
def test_fetch_dlo_schema_gives_up_after_three() -> None:
    for _ in range(3):
        responses.add(responses.GET, DLO_URL, status=500)
    with pytest.raises(streams.StreamsError):
        streams.fetch_dlo_schema(
            instance_url=INSTANCE_URL, access_token="TOK", dlo_name=DLO_NAME
        )
    assert len(responses.calls) == 3
