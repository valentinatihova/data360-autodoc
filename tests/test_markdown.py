"""Tests for the Markdown generator."""

from __future__ import annotations

from datetime import datetime, timezone

from generator.markdown import render_markdown
from models import (
    CalculatedInsight,
    DataLakeObject,
    DataModelObject,
    DataStream,
    DmoFieldMapping,
    FieldDef,
    FieldMapping,
    IdentityResolutionRuleset,
    Mapping,
    OrgSchema,
    Relationship,
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


def test_dmo_field_type_inferred_marker() -> None:
    schema = OrgSchema(
        org_name="Acme",
        instance_url="https://acme.my.salesforce.com",
        generated_at=FIXED_TS,
        dmos=(
            DataModelObject(
                name="ssot__Account__dlm",
                label="Account",
                fields=(
                    FieldDef(
                        name="ssot__Revenue__c", type="Number", type_inferred=True
                    ),
                    FieldDef(name="ssot__Other__c", type="Unknown"),
                ),
            ),
        ),
    )
    md = render_markdown(schema)
    # Inferred type carries the render-only marker; clean type token is untouched.
    assert "| ssot__Revenue__c | Number (via DLO) |  |" in md
    assert "| ssot__Other__c | Unknown |  |" in md


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


def test_data_streams_section_matches_sheet1_columns() -> None:
    schema = OrgSchema(
        org_name="Acme",
        instance_url="https://acme.my.salesforce.com",
        generated_at=FIXED_TS,
        streams=(
            DataStream(
                name="Account_CRM_Stream",
                dlo_name="Account_CRM__dll",
                dlo_label="Account_CRM",
                data_source="Salesforce CRM",
                category="Profile",
                event_time_field="CreatedDate",
                primary_keys=("Id",),
                refresh_mode="UPSERT",
                schedule_frequency="BATCH",
            ),
        ),
    )
    md = render_markdown(schema)

    assert "## Data Streams" in md
    # Exact Sheet 1 column header order.
    header = (
        "| DataSource | ObjectLabel | ApiName | Category | EventTimeField | "
        "PrimaryKey | FormulaField | FormulaCalculation | OrgUnitIdentifier | "
        "ScheduleFrequency | RefreshMode | DEExtractionMode | StreamName |"
    )
    assert header in md
    # Row values, including ApiName linking to the DLO.
    assert "Salesforce CRM" in md
    assert "Account_CRM__dll" in md
    assert "| Id |" in md or " Id |" in md
    assert "UPSERT" in md
    assert "BATCH" in md


def test_data_streams_empty_placeholder() -> None:
    schema = OrgSchema(
        org_name="Empty",
        instance_url="https://empty.my.salesforce.com",
        generated_at=FIXED_TS,
    )
    md = render_markdown(schema)
    assert "_No Data Streams found._" in md
    assert "_No field mappings found._" in md
    assert "_No DLO → DMO field mappings found._" in md


def test_field_mapping_section_columns_and_heuristics() -> None:
    schema = OrgSchema(
        org_name="Acme",
        instance_url="https://acme.my.salesforce.com",
        generated_at=FIXED_TS,
        field_mappings=(
            FieldMapping(
                stream_name="Account_CRM",
                source_field="Id",
                dlo_field_label="Account ID",
                dlo_field_name="Id",
                data_type="Text",
                is_primary_key=True,
                is_foreign_key=False,
                data_source="SalesforceDotCom",
            ),
            FieldMapping(
                stream_name="Account_CRM",
                source_field=None,
                dlo_field_label="KQ_Id",
                dlo_field_name="KQ_Id",
                data_type="Text",
                is_primary_key=False,
                is_foreign_key=True,
                data_source="SalesforceDotCom",
            ),
        ),
    )
    md = render_markdown(schema)

    assert "## Field Mapping (Streams → DLO)" in md
    header = (
        "| Mapped Data Stream | DLO API Name | Field Label Source | Field Label DLO "
        "| Data Type | Primary Key | Data Source | Foreign Key | Nullable |"
    )
    assert header in md
    # Heuristic + nullable note.
    assert "`KQ_`" in md
    assert "Nullable" in md and "never guessed" in md
    # PK row: DLO API Name blank (fixture), PK Yes, FK blank, Nullable blank.
    assert (
        "| Account_CRM |  | Id | Account ID | Text | Yes | SalesforceDotCom |  |  |"
        in md
    )
    # KQ_ row: source blank, Foreign Key Yes (heuristic), Nullable blank.
    assert "| Account_CRM |  |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |" in md


def test_dmo_field_mapping_section_grouped() -> None:
    schema = OrgSchema(
        org_name="Acme",
        instance_url="https://acme.my.salesforce.com",
        generated_at=FIXED_TS,
        dmo_field_mappings=(
            DmoFieldMapping(
                source_dlo_name="Account_CRM__dll",
                source_dlo_label="Account_CRM",
                source_field_name="Id_c",
                source_field_label="Id_c",
                target_dmo_name="ssot__Account__dlm",
                target_dmo_label="Account",
                target_field_name="ssot__Id__c",
                target_field_label="ssot__Id__c",
            ),
            DmoFieldMapping(
                source_dlo_name="Account_CRM__dll",
                source_dlo_label="Account_CRM",
                source_field_name="Name_c",
                source_field_label="Name_c",
                target_dmo_name="ssot__Account__dlm",
                target_dmo_label="Account",
                target_field_name="ssot__Name__c",
                target_field_label="ssot__Name__c",
            ),
            DmoFieldMapping(
                source_dlo_name="Other__dll",
                source_dlo_label="Other__dll",
                source_field_name="Foo_c",
                source_field_label="Foo_c",
                target_dmo_name="ssot__Contact__dlm",
                target_dmo_label="Contact",
                target_field_name="ssot__Foo__c",
                target_field_label="ssot__Foo__c",
            ),
        ),
    )
    md = render_markdown(schema)

    assert "## DLO → DMO Field Mappings" in md
    # All 11 columns, in Sheet 3 order (incl. the 3 sheet-structure columns).
    header = (
        "| Source DLO API Name | Source DLO Label | Source Field API Name | "
        "Source Field Label | Target DMO API Name | Target DMO Label | "
        "Target DMO Attribute API Name | Target Attribute Label | "
        "Data Source Field | Business Label | Manual Mapping |"
    )
    assert header in md
    # Grouped by source -> target pairing, one sub-header per pair.
    assert "### Account_CRM (`Account_CRM__dll`) → Account (`ssot__Account__dlm`)" in md
    assert "### Other__dll (`Other__dll`) → Contact (`ssot__Contact__dlm`)" in md
    # A full row; the 3 trailing structure columns are blank.
    assert (
        "| Account_CRM__dll | Account_CRM | Id_c | Id_c | ssot__Account__dlm | "
        "Account | ssot__Id__c | ssot__Id__c |  |  |  |" in md
    )
    # Curated-columns note present.
    assert "intentionally blank" in md


def test_relationships_section_renders_rows_and_blanks() -> None:
    schema = OrgSchema(
        org_name="Acme",
        instance_url="https://acme.my.salesforce.com",
        generated_at=FIXED_TS,
        relationships=(
            Relationship(
                source_dmo_name="ssot__Account__dlm",
                source_dmo_label="Account",
                source_field="ssot__PrimarySalesContactPointId__c",
                cardinality="N:1",
                related_entity="ssot__ContactPointEmail__dlm",
                related_field="ssot__Id__c",
                relationship_label="Account_..._N_1",
                status="INACTIVE",
            ),
            # A sparse row: only source object/field known — must still render.
            Relationship(
                source_dmo_name="ssot__Account__dlm",
                source_dmo_label="Account",
                source_field="ssot__Id__c",
            ),
        ),
    )
    md = render_markdown(schema)

    assert "## Relationships" in md
    assert (
        "| Object | Field | Cardinality | Related Object | Related Field "
        "| Status |" in md
    )
    # Status surfaced (inactive relationships are visible, not dropped); the
    # verbose relationship name stays out of the table (kept in JSON only).
    assert (
        "| Account | ssot__PrimarySalesContactPointId__c | N:1 "
        "| ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |" in md
    )
    # Sparse row rendered with blanks, not suppressed.
    assert "| Account | ssot__Id__c |  |  |  |  |" in md


def test_relationships_empty_placeholder() -> None:
    schema = OrgSchema(
        org_name="Empty",
        instance_url="https://empty.my.salesforce.com",
        generated_at=FIXED_TS,
    )
    assert "_No relationships found._" in render_markdown(schema)
