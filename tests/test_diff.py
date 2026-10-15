"""Tests for schema drift detection (``diff_schemas``) — pure, no I/O."""

from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

import pytest

from data360_autodoc.diff import ValueChange, diff_schemas
from data360_autodoc.generator.snapshot import load_json
from data360_autodoc.models import (
    DataLakeObject,
    DataModelObject,
    DmoFieldMapping,
    FieldDef,
    Mapping,
    OrgSchema,
    Relationship,
)

FIXTURES = Path(__file__).parent / "fixtures"
OLD_TS = datetime(2026, 10, 1, 6, 0, tzinfo=timezone.utc)
NEW_TS = datetime(2026, 10, 8, 6, 0, tzinfo=timezone.utc)


def _schema(**kwargs) -> OrgSchema:
    return OrgSchema(
        org_name="Acme Data Cloud",
        instance_url="https://acme.my.salesforce.com",
        generated_at=kwargs.pop("generated_at", OLD_TS),
        **kwargs,
    )


def _individual(*fields: FieldDef, label: str = "Individual") -> DataModelObject:
    return DataModelObject(name="Individual__dmo", label=label, fields=fields)


def _fm(source_field: str, target_field: str) -> DmoFieldMapping:
    return DmoFieldMapping(
        source_dlo_name="Contact_Home__dll",
        source_dlo_label="Contact (Home)",
        source_field_name=source_field,
        source_field_label=source_field,
        target_dmo_name="Individual__dmo",
        target_dmo_label="Individual",
        target_field_name=target_field,
        target_field_label=target_field,
    )


def _rel(**overrides) -> Relationship:
    base = Relationship(
        source_dmo_name="ContactPointEmail__dmo",
        source_dmo_label="Contact Point Email",
        source_field="PartyId__c",
        cardinality="N:1",
        related_entity="Individual__dmo",
        related_field="Id__c",
        relationship_label="CPEToIndividual",
        status="ACTIVE",
    )
    return replace(base, **overrides)


ID = FieldDef(name="Id__c", type="Text", is_key=True)
EMAIL = FieldDef(name="Email__c", type="Text")


# --------------------------------------------------------------------------- #
# No drift
# --------------------------------------------------------------------------- #


def test_identical_snapshots_have_no_changes() -> None:
    old = _schema(dmos=(_individual(ID, EMAIL),), relationships=(_rel(),))
    new = replace(old, generated_at=NEW_TS)  # timestamp alone is not drift
    diff = diff_schemas(old, new)
    assert not diff.has_changes
    assert diff.change_count == 0


def test_empty_snapshots_have_no_changes() -> None:
    assert not diff_schemas(_schema(), _schema()).has_changes


def test_input_order_does_not_matter() -> None:
    a = DataModelObject(name="A__dmo", label="A", fields=(ID, EMAIL))
    b = DataModelObject(name="B__dmo", label="B")
    old = _schema(dmos=(a, b))
    new = _schema(dmos=(b, replace(a, fields=(EMAIL, ID))))
    assert not diff_schemas(old, new).has_changes


def test_type_inferred_flag_alone_is_not_drift() -> None:
    old = _schema(dmos=(_individual(FieldDef("Rev__c", "Number")),))
    new = _schema(dmos=(_individual(FieldDef("Rev__c", "Number", type_inferred=True)),))
    assert not diff_schemas(old, new).has_changes


# --------------------------------------------------------------------------- #
# Objects + fields
# --------------------------------------------------------------------------- #


def test_added_and_removed_dmos() -> None:
    account = DataModelObject(name="Account__dmo", label="Account")
    old = _schema(dmos=(_individual(ID),))
    new = _schema(dmos=(account,))
    diff = diff_schemas(old, new)
    assert [o.name for o in diff.dmos.added] == ["Account__dmo"]
    assert [o.name for o in diff.dmos.removed] == ["Individual__dmo"]
    assert diff.dmos.changed == ()


def test_added_removed_and_changed_fields() -> None:
    old = _schema(dmos=(_individual(ID, EMAIL, FieldDef("Phone__c", "Text")),))
    new = _schema(
        dmos=(
            _individual(
                ID,
                FieldDef("Email__c", "EmailAddress"),
                FieldDef("BirthDate__c", "Date"),
            ),
        )
    )
    (change,) = diff_schemas(old, new).dmos.changed
    assert change.name == "Individual__dmo"
    assert [f.name for f in change.added_fields] == ["BirthDate__c"]
    assert [f.name for f in change.removed_fields] == ["Phone__c"]
    (field_change,) = change.changed_fields
    assert field_change.name == "Email__c"
    assert field_change.changes == (ValueChange("type", "Text", "EmailAddress"),)


def test_key_flag_and_qualifier_changes() -> None:
    old = _schema(
        dlos=(DataLakeObject("Order__dll", "Order", (FieldDef("OrderId", "Text"),)),)
    )
    new = _schema(
        dlos=(
            DataLakeObject(
                "Order__dll",
                "Order",
                (FieldDef("OrderId", "Text", is_key=True, key_qualifier="PrimaryKey"),),
            ),
        )
    )
    (change,) = diff_schemas(old, new).dlos.changed
    (field_change,) = change.changed_fields
    assert field_change.changes == (
        ValueChange("is_key", False, True),
        ValueChange("key_qualifier", None, "PrimaryKey"),
    )


def test_label_change_is_reported() -> None:
    old = _schema(dmos=(_individual(ID),))
    new = _schema(dmos=(_individual(ID, label="Person"),))
    diff = diff_schemas(old, new)
    (change,) = diff.dmos.changed
    assert change.changes == (ValueChange("label", "Individual", "Person"),)
    assert change.label == "Person"
    assert diff.change_count == 1


def test_dmos_and_dlos_are_diffed_independently() -> None:
    old = _schema(dlos=(DataLakeObject("X__dll", "X"),))
    new = _schema(dmos=(DataModelObject("X__dll", "X"),))
    diff = diff_schemas(old, new)
    assert [o.name for o in diff.dmos.added] == ["X__dll"]
    assert [o.name for o in diff.dlos.removed] == ["X__dll"]


# --------------------------------------------------------------------------- #
# Mappings + relationships
# --------------------------------------------------------------------------- #


def test_object_mapping_added_and_removed() -> None:
    old = _schema(mappings=(Mapping("Legacy__dll", "Individual__dmo"),))
    new = _schema(mappings=(Mapping("Contact_Home__dll", "Individual__dmo"),))
    diff = diff_schemas(old, new)
    assert diff.mappings_added == (Mapping("Contact_Home__dll", "Individual__dmo"),)
    assert diff.mappings_removed == (Mapping("Legacy__dll", "Individual__dmo"),)


def test_repointed_field_mapping_is_removed_plus_added() -> None:
    old = _schema(dmo_field_mappings=(_fm("Email", "Email__c"),))
    new = _schema(dmo_field_mappings=(_fm("Email", "PersonalEmail__c"),))
    diff = diff_schemas(old, new)
    assert [m.target_field_name for m in diff.field_mappings_added] == [
        "PersonalEmail__c"
    ]
    assert [m.target_field_name for m in diff.field_mappings_removed] == ["Email__c"]


def test_field_mapping_label_change_is_not_drift() -> None:
    old = _schema(dmo_field_mappings=(_fm("Email", "Email__c"),))
    new = _schema(
        dmo_field_mappings=(replace(_fm("Email", "Email__c"), source_field_label="E"),)
    )
    assert not diff_schemas(old, new).has_changes


def test_relationship_status_change() -> None:
    old = _schema(relationships=(_rel(),))
    new = _schema(relationships=(_rel(status="INACTIVE"),))
    diff = diff_schemas(old, new)
    (change,) = diff.relationships_changed
    assert change.changes == (ValueChange("status", "ACTIVE", "INACTIVE"),)
    assert diff.relationships_added == diff.relationships_removed == ()


def test_relationship_added_and_removed() -> None:
    old = _schema(relationships=(_rel(),))
    new = _schema(relationships=(_rel(source_field="AltPartyId__c"),))
    diff = diff_schemas(old, new)
    assert [r.source_field for r in diff.relationships_added] == ["AltPartyId__c"]
    assert [r.source_field for r in diff.relationships_removed] == ["PartyId__c"]


@pytest.mark.parametrize(
    "overrides,attribute",
    [
        ({"cardinality": "1:1"}, "cardinality"),
        ({"relationship_label": "Y"}, "relationship_label"),
    ],
)
def test_relationship_attribute_changes(overrides: dict, attribute: str) -> None:
    diff = diff_schemas(
        _schema(relationships=(_rel(),)), _schema(relationships=(_rel(**overrides),))
    )
    (change,) = diff.relationships_changed
    assert [c.attribute for c in change.changes] == [attribute]


# --------------------------------------------------------------------------- #
# Synthetic fixture pair (tests/fixtures/acme-*.json)
# --------------------------------------------------------------------------- #


def _fixture(name: str) -> OrgSchema:
    return load_json((FIXTURES / name).read_text(encoding="utf-8"))


def test_fixture_pair_summary() -> None:
    diff = diff_schemas(_fixture("acme-before.json"), _fixture("acme-after.json"))
    assert diff.summary() == {
        "dmos": {"added": 1, "removed": 0, "changed": 2},
        "dmo_fields": {"added": 2, "removed": 0, "changed": 1},
        "dlos": {"added": 1, "removed": 1, "changed": 2},
        "dlo_fields": {"added": 2, "removed": 0, "changed": 1},
        "mappings": {"added": 1, "removed": 1, "changed": 0},
        "field_mappings": {"added": 4, "removed": 1, "changed": 0},
        "relationships": {"added": 1, "removed": 0, "changed": 1},
    }
    # Changed objects are containers: their field changes are what count.
    assert diff.change_count == 18


def test_fixture_against_itself_is_clean() -> None:
    snapshot = _fixture("acme-after.json")
    assert not diff_schemas(snapshot, snapshot).has_changes
