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

from models import (
    CalculatedInsight,
    DataLakeObject,
    DataModelObject,
    FieldDef,
    IdentityResolutionRuleset,
    OrgSchema,
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
        rows.append(f"| {_escape(fd.name)} | {_escape(fd.type)} | {key} |")
    return rows


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
