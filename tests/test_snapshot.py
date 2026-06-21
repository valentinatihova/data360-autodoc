"""Tests for the JSON snapshot serializer (the drift-detection seam)."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import pytest

from generator.snapshot import (
    SNAPSHOT_VERSION,
    from_dict,
    load_json,
    render_json,
    to_dict,
)
from models import (
    CalculatedInsight,
    DataLakeObject,
    DataModelObject,
    FieldDef,
    IdentityResolutionRuleset,
    Mapping,
    OrgSchema,
)

FIXED_TS = datetime(2026, 6, 21, 17, 30, 0, tzinfo=timezone.utc)


def _schema() -> OrgSchema:
    return OrgSchema(
        org_name="Acme Data Cloud",
        instance_url="https://acme.my.salesforce.com",
        generated_at=FIXED_TS,
        dmos=(
            DataModelObject(
                name="Individual__dmo",
                label="Individual",
                fields=(FieldDef(name="Id__c", type="Text", is_key=True),),
            ),
        ),
        dlos=(
            DataLakeObject(
                name="Order_Home__dll",
                label="Order (Home)",
                fields=(
                    FieldDef(
                        name="OrderId",
                        type="Text",
                        is_key=True,
                        key_qualifier="PrimaryKey",
                    ),
                ),
            ),
        ),
        cios=(
            CalculatedInsight(
                name="CLV__cio",
                label="Customer Lifetime Value",
                dimensions=("Individual__dmo.Id__c",),
                measures=("TotalSpend",),
            ),
        ),
        identity_rulesets=(
            IdentityResolutionRuleset(
                name="Default_Ruleset",
                label="Default Ruleset",
                match_rules=("Exact Email",),
                reconciliation_rule="Most Recent",
            ),
        ),
        mappings=(Mapping(source_dlo="Order_Home__dll", target_dmo="Individual__dmo"),),
    )


def test_round_trip_is_lossless() -> None:
    schema = _schema()
    assert load_json(render_json(schema)) == schema


def test_round_trip_empty_schema() -> None:
    schema = OrgSchema(
        org_name="Empty",
        instance_url="https://empty.my.salesforce.com",
        generated_at=FIXED_TS,
    )
    assert load_json(render_json(schema)) == schema


def test_render_is_deterministic() -> None:
    schema = _schema()
    assert render_json(schema) == render_json(schema)


def test_snapshot_version_present() -> None:
    data = json.loads(render_json(_schema()))
    assert data["snapshot_version"] == SNAPSHOT_VERSION


def test_to_dict_is_json_safe() -> None:
    # to_dict output must serialize without custom encoders.
    json.dumps(to_dict(_schema()))


def test_from_dict_tolerates_missing_optionals() -> None:
    # A minimal snapshot (only required top-level keys) still loads.
    minimal = {
        "org_name": "Min",
        "instance_url": "https://min.my.salesforce.com",
        "generated_at": FIXED_TS.isoformat(),
    }
    schema = from_dict(minimal)
    assert schema.org_name == "Min"
    assert schema.dmos == ()
    assert schema.mappings == ()


def test_from_dict_rejects_unknown_version() -> None:
    data = json.loads(render_json(_schema()))
    data["snapshot_version"] = SNAPSHOT_VERSION + 1
    with pytest.raises(ValueError, match="Unsupported snapshot_version"):
        from_dict(data)


def test_from_dict_accepts_current_version() -> None:
    data = json.loads(render_json(_schema()))
    assert from_dict(data).org_name == "Acme Data Cloud"


def test_two_snapshots_diff_for_drift() -> None:
    # The whole point of the seam: a changed org yields a different snapshot.
    before = _schema()
    after = OrgSchema(
        org_name=before.org_name,
        instance_url=before.instance_url,
        generated_at=FIXED_TS,
        dmos=before.dmos + (DataModelObject(name="Account__dmo", label="Account"),),
        dlos=before.dlos,
        cios=before.cios,
        identity_rulesets=before.identity_rulesets,
        mappings=before.mappings,
    )
    assert render_json(before) != render_json(after)
    # And the loaded objects differ in exactly the new DMO.
    loaded_before = load_json(render_json(before))
    loaded_after = load_json(render_json(after))
    new_names = {d.name for d in loaded_after.dmos} - {
        d.name for d in loaded_before.dmos
    }
    assert new_names == {"Account__dmo"}
