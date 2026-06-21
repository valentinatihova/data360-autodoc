"""Tests for the Markdown generator."""

from __future__ import annotations

from datetime import datetime, timezone

from generator.markdown import render_markdown
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


def _full_schema() -> OrgSchema:
    return OrgSchema(
        org_name="Acme Data Cloud",
        instance_url="https://acme.my.salesforce.com",
        generated_at=FIXED_TS,
        dmos=(
            DataModelObject(
                name="Individual__dmo",
                label="Individual",
                fields=(
                    FieldDef(name="FirstName__c", type="Text"),
                    FieldDef(name="Id__c", type="Text", is_key=True),
                ),
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
                match_rules=("Exact Email", "Fuzzy Name"),
                reconciliation_rule="Most Recent",
            ),
        ),
        mappings=(Mapping(source_dlo="Order_Home__dll", target_dmo="Individual__dmo"),),
    )


def test_title_and_provenance() -> None:
    md = render_markdown(_full_schema())
    assert md.startswith("# Data 360 Documentation — Acme Data Cloud\n")
    assert "_Generated 2026-06-21 17:30:00 UTC · https://acme.my.salesforce.com_" in md


def test_all_sections_present() -> None:
    md = render_markdown(_full_schema())
    assert "## Data Model Objects (DMOs)" in md
    assert "## Data Lake Objects (DLOs)" in md
    assert "## Identity Resolution Rules" in md
    assert "## Calculated Insights" in md


def test_field_table_key_column() -> None:
    md = render_markdown(_full_schema())
    # DLO field has a key_qualifier -> shows the qualifier text.
    assert "| OrderId | Text | PrimaryKey |" in md
    # DMO key field has is_key but no qualifier -> check mark.
    assert "| Id__c | Text | ✓ |" in md
    # Non-key field -> blank key cell.
    assert "| FirstName__c | Text |  |" in md


def test_object_heading_shows_label_and_name() -> None:
    md = render_markdown(_full_schema())
    assert "### Order (Home) (`Order_Home__dll`)" in md
    assert "### Individual (`Individual__dmo`)" in md


def test_identity_and_ci_details() -> None:
    md = render_markdown(_full_schema())
    assert "- **Reconciliation:** Most Recent" in md
    assert "  - Exact Email" in md
    assert "- **Dimensions:** Individual__dmo.Id__c" in md
    assert "- **Measures:** TotalSpend" in md


def test_deterministic_output() -> None:
    schema = _full_schema()
    assert render_markdown(schema) == render_markdown(schema)


def test_empty_schema_renders_placeholders() -> None:
    schema = OrgSchema(
        org_name="Empty Org",
        instance_url="https://empty.my.salesforce.com",
        generated_at=FIXED_TS,
    )
    md = render_markdown(schema)
    assert "_No Data Model Objects found._" in md
    assert "_No Data Lake Objects found._" in md
    assert "_No Identity Resolution Rules found._" in md
    assert "_No Calculated Insights found._" in md


def test_pipe_in_cell_is_escaped() -> None:
    schema = OrgSchema(
        org_name="Pipe Org",
        instance_url="https://x.my.salesforce.com",
        generated_at=FIXED_TS,
        dmos=(
            DataModelObject(
                name="Weird__dmo",
                label="Weird",
                fields=(FieldDef(name="a|b", type="Text|Rich"),),
            ),
        ),
    )
    md = render_markdown(schema)
    # The literal pipe is escaped so it cannot split the table cell.
    assert "| a\\|b | Text\\|Rich |  |" in md


def test_object_with_no_fields() -> None:
    schema = OrgSchema(
        org_name="NoFields",
        instance_url="https://x.my.salesforce.com",
        generated_at=FIXED_TS,
        dmos=(DataModelObject(name="Bare__dmo", label="Bare", fields=()),),
    )
    md = render_markdown(schema)
    assert "_No fields._" in md
