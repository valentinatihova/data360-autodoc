"""Markdown generator for a Data 360 org.

Pure function of :class:`~models.OrgSchema` -> Markdown string. Because the
schema is already sorted alphabetically and ``generated_at`` is an input (not a
wall-clock read), the same ``OrgSchema`` always renders byte-identical output —
the project's determinism guarantee.

Document shape::

    # Data 360 Documentation — <org name>
    _Generated <timestamp> · <instance_url>_

    ## Data Model Objects (DMOs)
    ### <label> (`<name>`)
    | Name | Type | Key |
    | ...  | ...  | ... |

    ## Data Lake Objects (DLOs)        (same field-table shape as DMOs)
    ## Identity Resolution Rules
    ## Calculated Insights
"""

from __future__ import annotations

from datetime import timezone
from itertools import groupby

from data360_autodoc.models import (
    CalculatedInsight,
    DataLakeObject,
    DataModelObject,
    DataStream,
    DmoFieldMapping,
    FieldDef,
    FieldMapping,
    IdentityResolutionRuleset,
    OrgSchema,
    Relationship,
)

#: Field Mapping (Sheet 2) table columns.
_FIELD_MAPPING_COLUMNS = (
    "Mapped Data Stream",
    "DLO API Name",
    "Field Label Source",
    "Field Label DLO",
    "Data Type",
    "Primary Key",
    "Data Source",
    "Foreign Key",
    "Nullable",
)

#: DLO → DMO Field Mappings (Sheet 3) table columns, in the SI doc's order.
#: The last three are sheet-structure columns: ``Data Source Field`` is filled
#: only when the mapping payload exposes a source-field reference; ``Business
#: Label`` and ``Manual Mapping`` are curated/manual and stay blank (the tool
#: never fabricates glossary content).
_DMO_FIELD_MAPPING_COLUMNS = (
    "Source DLO API Name",
    "Source DLO Label",
    "Source Field API Name",
    "Source Field Label",
    "Target DMO API Name",
    "Target DMO Label",
    "Target DMO Attribute API Name",
    "Target Attribute Label",
    "Data Source Field",
    "Business Label",
    "Manual Mapping",
)

#: Data Streams table columns, in the order of the SI doc's Sheet 1.
_STREAM_COLUMNS = (
    "DataSource",
    "ObjectLabel",
    "ApiName",
    "Category",
    "EventTimeField",
    "PrimaryKey",
    "FormulaField",
    "FormulaCalculation",
    "OrgUnitIdentifier",
    "ScheduleFrequency",
    "RefreshMode",
    "DEExtractionMode",
    "StreamName",
)


def render_markdown(schema: OrgSchema) -> str:
    """Render an :class:`~models.OrgSchema` as a single Markdown string.

    Args:
        schema: The normalized org snapshot to document.

    Returns:
        A Markdown document. Deterministic: identical ``schema`` in, identical
        string out.
    """
    lines: list[str] = []
    lines.append(f"# Data 360 Documentation — {_escape(schema.org_name)}")
    lines.append("")
    timestamp = schema.generated_at.astimezone(timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )
    lines.append(f"_Generated {timestamp} · {_escape(schema.instance_url)}_")
    lines.append("")

    lines.extend(_render_object_section("Data Model Objects (DMOs)", schema.dmos))
    lines.extend(_render_object_section("Data Lake Objects (DLOs)", schema.dlos))
    lines.extend(_render_streams_section(schema.streams))
    lines.extend(_render_field_mapping_section(schema.field_mappings))
    lines.extend(_render_dmo_field_mapping_section(schema.dmo_field_mappings))
    lines.extend(_render_relationships_section(schema.relationships))
    lines.extend(_render_identity_section(schema.identity_rulesets))
    lines.extend(_render_ci_section(schema.cios))

    # Single trailing newline, no double-blank at EOF.
    return "\n".join(lines).rstrip("\n") + "\n"


def _render_object_section(
    title: str,
    objects: tuple[DataModelObject, ...] | tuple[DataLakeObject, ...],
) -> list[str]:
    """Render a DMO or DLO section: heading + one field table per object."""
    lines = [f"## {title}", ""]
    if not objects:
        lines.append(f"_No {title.split(' (')[0]} found._")
        lines.append("")
        return lines
    for obj in objects:
        lines.append(f"### {_escape(obj.label)} (`{_escape(obj.name)}`)")
        lines.append("")
        lines.extend(_render_fields_table(obj.fields))
        lines.append("")
    return lines


def _render_fields_table(fields: tuple[FieldDef, ...]) -> list[str]:
    """Render the shared ``Name | Type | Key`` table for a set of fields.

    The ``Key`` cell shows the ``key_qualifier`` when present, falls back to a
    check mark when the field is a key without a qualifier, and is blank
    otherwise.
    """
    if not fields:
        return ["_No fields._"]
    rows = ["| Name | Type | Key |", "| --- | --- | --- |"]
    for fd in fields:
        if fd.key_qualifier:
            key = _escape(fd.key_qualifier)
        elif fd.is_key:
            key = "✓"
        else:
            key = ""
        # Provenance marker is render-only; the stored type token stays clean.
        type_cell = _escape(fd.type)
        if fd.type_inferred:
            type_cell += " (via DLO)"
        rows.append(f"| {_escape(fd.name)} | {type_cell} | {key} |")
    return rows


def _render_streams_section(streams: tuple[DataStream, ...]) -> list[str]:
    """Render the Data Streams section: one row per stream, Sheet 1 columns.

    ``ApiName`` is the DLO the stream populates, linking each row to its DLO in
    the Data Lake Objects section. Missing values render as blank cells.
    """
    lines = ["## Data Streams", ""]
    if not streams:
        lines.append("_No Data Streams found._")
        lines.append("")
        return lines
    lines.append(
        "Source and refresh metadata per stream. **ApiName** is the DLO it "
        "populates (see the Data Lake Objects section above)."
    )
    lines.append("")
    lines.append("| " + " | ".join(_STREAM_COLUMNS) + " |")
    lines.append("| " + " | ".join("---" for _ in _STREAM_COLUMNS) + " |")
    for s in streams:
        cells = (
            s.data_source,
            s.dlo_label,
            s.dlo_name,
            s.category,
            s.event_time_field,
            ", ".join(s.primary_keys),
            ", ".join(s.formula_fields),
            ", ".join(s.formula_calculations),
            s.org_unit_identifier,
            s.schedule_frequency,
            s.refresh_mode,
            s.de_extraction_mode,
            s.name,
        )
        lines.append("| " + " | ".join(_escape(c) if c else "" for c in cells) + " |")
    lines.append("")
    return lines


def _render_field_mapping_section(rows: tuple[FieldMapping, ...]) -> list[str]:
    """Render the Source → DLO field-mapping section (the SI doc's Sheet 2).

    One row per DLO field. Foreign Key is heuristic (``KQ_`` prefix); Nullable is
    not exposed by the data-streams endpoint and is always blank.
    """
    lines = ["## Field Mapping (Streams → DLO)", ""]
    if not rows:
        lines.append("_No field mappings found._")
        lines.append("")
        return lines
    lines.append(
        "One row per Data Lake field. **DLO API Name** is the Data Lake Object the "
        "stream populates. **Foreign Key** is heuristic — flagged for fields whose "
        "API name starts with `KQ_` (Data Cloud Key Qualifier pattern). "
        "**Nullable** is shown only where the source exposes it; "
        "`/ssot/data-streams` does not, so it stays blank for these streams (it is "
        "never guessed)."
    )
    lines.append("")
    lines.append("| " + " | ".join(_FIELD_MAPPING_COLUMNS) + " |")
    lines.append("| " + " | ".join("---" for _ in _FIELD_MAPPING_COLUMNS) + " |")
    for r in rows:
        cells = (
            r.stream_name,
            r.dlo_name,
            r.source_field or "",
            r.dlo_field_label,
            r.data_type,
            "Yes" if r.is_primary_key else "No",
            r.data_source or "",
            "Yes" if r.is_foreign_key else "",
            _yes_no_blank(r.nullable),
        )
        lines.append("| " + " | ".join(_escape(c) if c else "" for c in cells) + " |")
    lines.append("")
    return lines


def _render_dmo_field_mapping_section(
    rows: tuple[DmoFieldMapping, ...],
) -> list[str]:
    """Render the DLO → DMO field-mapping section (the SI doc's Sheet 3).

    Rows are grouped by their ``(Source DLO, Target DMO)`` pairing, each under a
    sub-heading. Labels are real where the mapping payload or the joined DLO
    field metadata supplies them; they fall back to the API name only when no
    label is available. The last three columns are sheet-structure columns
    (mostly manual/curated) — see :data:`_DMO_FIELD_MAPPING_COLUMNS`.
    """
    lines = ["## DLO → DMO Field Mappings", ""]
    if not rows:
        lines.append("_No DLO → DMO field mappings found._")
        lines.append("")
        return lines
    lines.append(
        "Field-level mappings from Data Lake Objects to Data Model Objects, "
        "grouped by source → target pairing. Labels are taken from the mapping "
        "payload and the joined DLO field metadata; an API name shown as a label "
        "means no human label was available. **Business Label** and **Manual "
        "Mapping** are curated columns and are intentionally blank here."
    )
    lines.append("")
    for (src_dlo, tgt_dmo), group in groupby(
        rows, key=lambda r: (r.source_dlo_name, r.target_dmo_name)
    ):
        group_rows = list(group)
        src_label = group_rows[0].source_dlo_label
        tgt_label = group_rows[0].target_dmo_label
        lines.append(
            f"### {_escape(src_label)} (`{_escape(src_dlo)}`) → "
            f"{_escape(tgt_label)} (`{_escape(tgt_dmo)}`)"
        )
        lines.append("")
        lines.append("| " + " | ".join(_DMO_FIELD_MAPPING_COLUMNS) + " |")
        lines.append(
            "| " + " | ".join("---" for _ in _DMO_FIELD_MAPPING_COLUMNS) + " |"
        )
        for r in group_rows:
            cells = (
                r.source_dlo_name,
                r.source_dlo_label,
                r.source_field_name,
                r.source_field_label,
                r.target_dmo_name,
                r.target_dmo_label,
                r.target_field_name,
                r.target_field_label,
                r.data_source_field or "",
                r.business_label or "",
                r.manual_mapping or "",
            )
            lines.append(
                "| " + " | ".join(_escape(c) if c else "" for c in cells) + " |"
            )
        lines.append("")
    return lines


def _render_relationships_section(
    rows: tuple[Relationship, ...],
) -> list[str]:
    """Render the Relationships section (the SI doc's Relationships sheet).

    One row per DMO relationship, from ``/ssot/data-model-objects/{dmo}/
    relationships``. Columns the org does not expose (related entity/field,
    cardinality) render blank rather than dropping the row.
    """
    columns = (
        "Object",
        "Field",
        "Cardinality",
        "Related Object",
        "Related Field",
        "Status",
    )
    lines = ["## Relationships", ""]
    if not rows:
        lines.append("_No relationships found._")
        lines.append("")
        return lines
    lines.append(
        "DMO-to-DMO relationships, read from `sourceObject`/`targetObject` in the "
        "relationships payload. **Object** is the source entity; **Related "
        "Object** is what it links to. **Status** is shown so inactive standard "
        "relationships are visible (not dropped). Blank cells mean the payload "
        "did not expose that property."
    )
    lines.append("")
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for r in rows:
        cells = (
            r.source_dmo_label or r.source_dmo_name,
            r.source_field or "",
            r.cardinality or "",
            r.related_entity or "",
            r.related_field or "",
            r.status or "",
        )
        lines.append("| " + " | ".join(_escape(c) if c else "" for c in cells) + " |")
    lines.append("")
    return lines


def _yes_no_blank(value: bool | None) -> str:
    """Render a tri-state boolean: ``Yes``/``No``/blank (``None`` = unknown)."""
    if value is None:
        return ""
    return "Yes" if value else "No"


def _render_identity_section(
    rulesets: tuple[IdentityResolutionRuleset, ...],
) -> list[str]:
    """Render the Identity Resolution Rules section."""
    lines = ["## Identity Resolution Rules", ""]
    if not rulesets:
        lines.append("_No Identity Resolution Rules found._")
        lines.append("")
        return lines
    for rs in rulesets:
        lines.append(f"### {_escape(rs.label)} (`{_escape(rs.name)}`)")
        lines.append("")
        if rs.match_rules:
            lines.append("- **Match rules:**")
            for rule in rs.match_rules:
                lines.append(f"  - {_escape(rule)}")
        else:
            lines.append("- **Match rules:** _none_")
        reconciliation = rs.reconciliation_rule or "_none_"
        lines.append(f"- **Reconciliation:** {_escape(reconciliation)}")
        lines.append("")
    return lines


def _render_ci_section(cios: tuple[CalculatedInsight, ...]) -> list[str]:
    """Render the Calculated Insights section."""
    lines = ["## Calculated Insights", ""]
    if not cios:
        lines.append("_No Calculated Insights found._")
        lines.append("")
        return lines
    for cio in cios:
        lines.append(f"### {_escape(cio.label)} (`{_escape(cio.name)}`)")
        lines.append("")
        dimensions = ", ".join(_escape(d) for d in cio.dimensions) or "_none_"
        measures = ", ".join(_escape(m) for m in cio.measures) or "_none_"
        lines.append(f"- **Dimensions:** {dimensions}")
        lines.append(f"- **Measures:** {measures}")
        lines.append("")
    return lines


def _escape(value: str) -> str:
    """Escape Markdown table-breaking characters in org-supplied text.

    Pipes would split table cells; backticks would open stray code spans;
    newlines would break row structure. Replace them so untrusted org data
    can never corrupt the rendered document.
    """
    return (
        value.replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("`", "\\`")
        .replace("\r\n", " ")
        .replace("\n", " ")
        .replace("\r", " ")
    )
