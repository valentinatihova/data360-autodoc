"""Drift report generators: turn a :class:`~diff.SchemaDiff` into artifacts.

Two outputs, both deterministic (the diff is already sorted):

- :func:`render_diff_markdown` — a human-readable change report, safe to post
  as a PR comment, a GitHub Actions job summary, or a client changelog.
- :func:`render_diff_json` — a machine-readable report for scripts and CI.

Report shape (Markdown)::

    # Data 360 Schema Drift — <new org name>
    _Old: <timestamp> · <instance_url>_
    _New: <timestamp> · <instance_url>_

    **N changes detected.**            (or "No schema drift detected.")
    | Area | Added | Removed | Changed |

    ## Data Model Objects (DMOs)       (only areas with changes are rendered)
    ## Data Lake Objects (DLOs)
    ## Data Streams
    ## DLO → DMO Mappings
    ## Relationships
"""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any

from data360_autodoc.diff import (
    ObjectDiff,
    SchemaDiff,
    SnapshotInfo,
    ValueChange,
)
from data360_autodoc.generator.markdown import _escape, _timestamp
from data360_autodoc.models import FieldDef, FieldMapping, Relationship

#: Bump when the JSON report shape changes incompatibly.
DIFF_REPORT_VERSION = 1

#: Summary-table rows: (summary key, display name).
_SUMMARY_ROWS = (
    ("dmos", "DMOs"),
    ("dmo_fields", "DMO fields"),
    ("dlos", "DLOs"),
    ("dlo_fields", "DLO fields"),
    ("streams", "Data streams"),
    ("stream_fields", "Stream → DLO field mappings"),
    ("mappings", "DLO → DMO object mappings"),
    ("field_mappings", "DLO → DMO field mappings"),
    ("relationships", "Relationships"),
)


def render_diff_markdown(diff: SchemaDiff) -> str:
    """Render a :class:`~diff.SchemaDiff` as a Markdown change report."""
    lines: list[str] = []
    org = diff.new.org_name
    if diff.old.org_name != org:
        org = f"{diff.old.org_name} → {org}"
    lines.append(f"# Data 360 Schema Drift — {_escape(org)}")
    lines.append("")
    lines.append(f"_Old: {_snapshot_line(diff.old)}_  ")
    lines.append(f"_New: {_snapshot_line(diff.new)}_")
    lines.append("")
    for warning in diff.warnings:
        lines.append(f"> ⚠️ {_escape(warning)}")
        lines.append("")

    if not diff.has_changes:
        lines.append("**No schema drift detected.**")
        return "\n".join(lines) + "\n"

    count = diff.change_count
    lines.append(f"**{count} change{'s' if count != 1 else ''} detected.**")
    lines.append("")
    lines.append("| Area | Added | Removed | Changed |")
    lines.append("| --- | --- | --- | --- |")
    summary = diff.summary()
    for key, name in _SUMMARY_ROWS:
        area = summary[key]
        if any(area.values()):
            changed = "—" if key in ("mappings", "field_mappings") else area["changed"]
            lines.append(
                f"| {name} | {area['added']} | {area['removed']} | {changed} |"
            )
    lines.append("")

    lines.extend(_render_objects("Data Model Objects (DMOs)", diff.dmos))
    lines.extend(_render_objects("Data Lake Objects (DLOs)", diff.dlos))
    lines.extend(_render_streams(diff))
    lines.extend(_render_mappings(diff))
    lines.extend(_render_relationships(diff))
    return "\n".join(lines).rstrip("\n") + "\n"


def render_diff_json(diff: SchemaDiff) -> str:
    """Serialize a :class:`~diff.SchemaDiff` to a deterministic JSON string."""
    return json.dumps(diff_to_dict(diff), indent=2, ensure_ascii=False) + "\n"


def diff_to_dict(diff: SchemaDiff) -> dict[str, Any]:
    """Convert a :class:`~diff.SchemaDiff` to a plain, JSON-safe dict."""
    return {
        "diff_report_version": DIFF_REPORT_VERSION,
        "old": _info_to_dict(diff.old),
        "new": _info_to_dict(diff.new),
        "warnings": list(diff.warnings),
        "has_changes": diff.has_changes,
        "change_count": diff.change_count,
        "summary": diff.summary(),
        "dmos": _objects_to_dict(diff.dmos),
        "dlos": _objects_to_dict(diff.dlos),
        "streams": {
            "added": [asdict(s) for s in diff.streams_added],
            "removed": [asdict(s) for s in diff.streams_removed],
            "changed": [
                {
                    "name": c.stream.name,
                    "changes": [asdict(v) for v in c.changes],
                }
                for c in diff.streams_changed
            ],
        },
        "stream_fields": {
            "added": [asdict(m) for m in diff.stream_fields_added],
            "removed": [asdict(m) for m in diff.stream_fields_removed],
            "changed": [
                {
                    "stream_name": c.mapping.stream_name,
                    "dlo_field_name": c.mapping.dlo_field_name,
                    "changes": [asdict(v) for v in c.changes],
                }
                for c in diff.stream_fields_changed
            ],
        },
        "mappings": {
            "added": [asdict(m) for m in diff.mappings_added],
            "removed": [asdict(m) for m in diff.mappings_removed],
        },
        "field_mappings": {
            "added": [asdict(m) for m in diff.field_mappings_added],
            "removed": [asdict(m) for m in diff.field_mappings_removed],
        },
        "relationships": {
            "added": [asdict(r) for r in diff.relationships_added],
            "removed": [asdict(r) for r in diff.relationships_removed],
            "changed": [
                {
                    **asdict(c.relationship),
                    "changes": [asdict(v) for v in c.changes],
                }
                for c in diff.relationships_changed
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Markdown sections
# --------------------------------------------------------------------------- #


def _snapshot_line(info: SnapshotInfo) -> str:
    return f"{_timestamp(info.generated_at)} · {_escape(info.instance_url)}"


def _render_objects(title: str, objects: ObjectDiff) -> list[str]:
    """Render added / removed / changed DMOs or DLOs; nothing if unchanged."""
    if not (objects.added or objects.removed or objects.changed):
        return []
    lines = [f"## {title}", ""]
    for heading, items in (("Added", objects.added), ("Removed", objects.removed)):
        if not items:
            continue
        lines.append(f"### {heading}")
        lines.append("")
        for obj in items:
            n = len(obj.fields)
            lines.append(
                f"- {_escape(obj.label)} (`{_escape(obj.name)}`) — "
                f"{n} field{'s' if n != 1 else ''}"
            )
        lines.append("")
    if objects.changed:
        lines.append("### Changed")
        lines.append("")
        for change in objects.changed:
            lines.append(f"#### {_escape(change.label)} (`{_escape(change.name)}`)")
            lines.append("")
            for value in change.changes:
                lines.append(f"- {_describe_change(value)}")
            if change.changes:
                lines.append("")
            rows = (
                [("added", f.name, _describe_field(f)) for f in change.added_fields]
                + [
                    ("removed", f.name, _describe_field(f))
                    for f in change.removed_fields
                ]
                + [
                    ("changed", fc.name, "; ".join(map(_describe_change, fc.changes)))
                    for fc in change.changed_fields
                ]
            )
            if rows:
                lines.append("| Change | Field | Details |")
                lines.append("| --- | --- | --- |")
                for kind, name, details in rows:
                    lines.append(f"| {kind} | {_escape(name)} | {details} |")
                lines.append("")
    return lines


def _render_streams(diff: SchemaDiff) -> list[str]:
    """Render data stream and Stream → DLO field mapping changes."""
    stream_rows = (
        [("added", s.name, f"→ {_escape(s.dlo_name)}") for s in diff.streams_added]
        + [
            ("removed", s.name, f"→ {_escape(s.dlo_name)}")
            for s in diff.streams_removed
        ]
        + [
            ("changed", c.stream.name, "; ".join(map(_describe_change, c.changes)))
            for c in diff.streams_changed
        ]
    )
    field_rows = (
        [("added", m, _describe_stream_field(m)) for m in diff.stream_fields_added]
        + [
            ("removed", m, _describe_stream_field(m))
            for m in diff.stream_fields_removed
        ]
        + [
            ("changed", c.mapping, "; ".join(map(_describe_change, c.changes)))
            for c in diff.stream_fields_changed
        ]
    )
    if not (stream_rows or field_rows):
        return []
    lines = ["## Data Streams", ""]
    if stream_rows:
        lines.append("| Change | Stream | Details |")
        lines.append("| --- | --- | --- |")
        for kind, name, details in stream_rows:
            lines.append(f"| {kind} | {_escape(name)} | {details} |")
        lines.append("")
    if field_rows:
        lines.append("### Stream → DLO field mappings")
        lines.append("")
        lines.append("| Change | Stream | DLO Field | Details |")
        lines.append("| --- | --- | --- | --- |")
        for kind, m, details in field_rows:
            lines.append(
                f"| {kind} | {_escape(m.stream_name)} "
                f"| {_escape(m.dlo_field_name)} | {details} |"
            )
        lines.append("")
    return lines


def _render_mappings(diff: SchemaDiff) -> list[str]:
    """Render object- and field-level DLO → DMO mapping changes."""
    if not (
        diff.mappings_added
        or diff.mappings_removed
        or diff.field_mappings_added
        or diff.field_mappings_removed
    ):
        return []
    lines = ["## DLO → DMO Mappings", ""]
    object_rows = [("added", m) for m in diff.mappings_added] + [
        ("removed", m) for m in diff.mappings_removed
    ]
    if object_rows:
        lines.append("| Change | Source DLO | Target DMO |")
        lines.append("| --- | --- | --- |")
        for kind, m in object_rows:
            lines.append(
                f"| {kind} | {_escape(m.source_dlo)} | {_escape(m.target_dmo)} |"
            )
        lines.append("")
    field_rows = [("added", m) for m in diff.field_mappings_added] + [
        ("removed", m) for m in diff.field_mappings_removed
    ]
    if field_rows:
        lines.append("### Field mappings")
        lines.append("")
        lines.append(
            "| Change | Source DLO | Source Field | Target DMO | Target Field |"
        )
        lines.append("| --- | --- | --- | --- | --- |")
        for kind, fm in field_rows:
            lines.append(
                f"| {kind} | {_escape(fm.source_dlo_name)} "
                f"| {_escape(fm.source_field_name)} "
                f"| {_escape(fm.target_dmo_name)} "
                f"| {_escape(fm.target_field_name)} |"
            )
        lines.append("")
    return lines


def _render_relationships(diff: SchemaDiff) -> list[str]:
    """Render added / removed / changed DMO relationships."""
    rows = (
        [("added", r, _describe_relationship(r)) for r in diff.relationships_added]
        + [
            ("removed", r, _describe_relationship(r))
            for r in diff.relationships_removed
        ]
        + [
            (
                "changed",
                c.relationship,
                "; ".join(map(_describe_change, c.changes)),
            )
            for c in diff.relationships_changed
        ]
    )
    if not rows:
        return []
    lines = ["## Relationships", ""]
    lines.append(
        "| Change | Object | Field | Related Object | Related Field | Details |"
    )
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for kind, r, details in rows:
        lines.append(
            f"| {kind} | {_escape(r.source_dmo_name)} "
            f"| {_escape(r.source_field or '')} "
            f"| {_escape(r.related_entity or '')} "
            f"| {_escape(r.related_field or '')} "
            f"| {details} |"
        )
    lines.append("")
    return lines


def _describe_field(f: FieldDef) -> str:
    """``Text``, ``Text, key: PrimaryKey`` or ``Text, key``."""
    text = _escape(f.type)
    if f.key_qualifier:
        text += f", key: {_escape(f.key_qualifier)}"
    elif f.is_key:
        text += ", key"
    return text


def _describe_stream_field(m: FieldMapping) -> str:
    """``Text``, ``Text, primary key`` — plus the source field when known."""
    text = _escape(m.data_type)
    if m.is_primary_key:
        text += ", primary key"
    if m.source_field:
        text += f", from {_escape(m.source_field)}"
    return text


def _describe_relationship(r: Relationship) -> str:
    parts = []
    if r.cardinality:
        parts.append(_escape(r.cardinality))
    if r.status:
        parts.append(_escape(r.status))
    return ", ".join(parts)


def _describe_change(change: ValueChange) -> str:
    """``type: Text → Number`` (``∅`` stands for an empty/missing value)."""
    return (
        f"{change.attribute}: {_format_value(change.old)} → "
        f"{_format_value(change.new)}"
    )


def _format_value(value: Any) -> str:
    if value is None or value == "" or value == ():
        return "∅"
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, tuple):
        return ", ".join(_escape(str(v)) for v in value)
    return _escape(str(value))


# --------------------------------------------------------------------------- #
# JSON helpers
# --------------------------------------------------------------------------- #


def _info_to_dict(info: SnapshotInfo) -> dict[str, Any]:
    return {
        "org_name": info.org_name,
        "instance_url": info.instance_url,
        "generated_at": info.generated_at.isoformat(),
    }


def _objects_to_dict(objects: ObjectDiff) -> dict[str, Any]:
    return {
        "added": [asdict(o) for o in objects.added],
        "removed": [asdict(o) for o in objects.removed],
        "changed": [
            {
                "name": c.name,
                "label": c.label,
                "changes": [asdict(v) for v in c.changes],
                "fields": {
                    "added": [asdict(f) for f in c.added_fields],
                    "removed": [asdict(f) for f in c.removed_fields],
                    "changed": [
                        {
                            "name": fc.name,
                            "changes": [asdict(v) for v in fc.changes],
                        }
                        for fc in c.changed_fields
                    ],
                },
            }
            for c in objects.changed
        ],
    }
