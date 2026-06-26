"""JSON snapshot serializer for an OrgSchema.

This is a first-class output format *and* the seam the paid drift-detection tier
builds on. A run can write ``snapshot.json``; a later run can load yesterday's
snapshot and diff it against today's freshly fetched schema. Because the
serialization is deterministic and round-trips losslessly
(``from_dict(to_dict(s)) == s``), drift detection reduces to comparing two
``OrgSchema`` values.

The ``snapshot_version`` field is written so future format changes can be
migrated rather than silently misread when diffing across tool versions.
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from data360_autodoc.models import (
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

#: Bump when the on-disk shape changes in a way that affects diffing.
SNAPSHOT_VERSION = 1


def render_json(schema: OrgSchema) -> str:
    """Serialize an :class:`~models.OrgSchema` to a deterministic JSON string.

    Args:
        schema: The org snapshot to serialize.

    Returns:
        Pretty-printed JSON (2-space indent, trailing newline). Identical
        ``schema`` in, identical string out — diff-friendly and drift-ready.
    """
    return json.dumps(to_dict(schema), indent=2, ensure_ascii=False) + "\n"


def load_json(text: str) -> OrgSchema:
    """Parse a snapshot JSON string back into an :class:`~models.OrgSchema`."""
    return from_dict(json.loads(text))


def to_dict(schema: OrgSchema) -> dict[str, Any]:
    """Convert an :class:`~models.OrgSchema` to a plain, JSON-safe dict."""
    return {
        "snapshot_version": SNAPSHOT_VERSION,
        "org_name": schema.org_name,
        "instance_url": schema.instance_url,
        "generated_at": schema.generated_at.isoformat(),
        "dmos": [_object_to_dict(o) for o in schema.dmos],
        "dlos": [_object_to_dict(o) for o in schema.dlos],
        "cios": [
            {
                "name": c.name,
                "label": c.label,
                "dimensions": list(c.dimensions),
                "measures": list(c.measures),
            }
            for c in schema.cios
        ],
        "identity_rulesets": [
            {
                "name": r.name,
                "label": r.label,
                "match_rules": list(r.match_rules),
                "reconciliation_rule": r.reconciliation_rule,
            }
            for r in schema.identity_rulesets
        ],
        "mappings": [
            {"source_dlo": m.source_dlo, "target_dmo": m.target_dmo}
            for m in schema.mappings
        ],
        "streams": [
            {
                "name": s.name,
                "dlo_name": s.dlo_name,
                "dlo_label": s.dlo_label,
                "data_source": s.data_source,
                "category": s.category,
                "event_time_field": s.event_time_field,
                "primary_keys": list(s.primary_keys),
                "formula_fields": list(s.formula_fields),
                "formula_calculations": list(s.formula_calculations),
                "org_unit_identifier": s.org_unit_identifier,
                "schedule_frequency": s.schedule_frequency,
                "refresh_mode": s.refresh_mode,
                "de_extraction_mode": s.de_extraction_mode,
            }
            for s in schema.streams
        ],
        "field_mappings": [
            {
                "stream_name": fm.stream_name,
                "source_field": fm.source_field,
                "dlo_field_label": fm.dlo_field_label,
                "dlo_field_name": fm.dlo_field_name,
                "data_type": fm.data_type,
                "is_primary_key": fm.is_primary_key,
                "is_foreign_key": fm.is_foreign_key,
                "data_source": fm.data_source,
                "dlo_name": fm.dlo_name,
                "nullable": fm.nullable,
            }
            for fm in schema.field_mappings
        ],
        "dmo_field_mappings": [
            {
                "source_dlo_name": d.source_dlo_name,
                "source_dlo_label": d.source_dlo_label,
                "source_field_name": d.source_field_name,
                "source_field_label": d.source_field_label,
                "target_dmo_name": d.target_dmo_name,
                "target_dmo_label": d.target_dmo_label,
                "target_field_name": d.target_field_name,
                "target_field_label": d.target_field_label,
                "data_source_field": d.data_source_field,
                "business_label": d.business_label,
                "manual_mapping": d.manual_mapping,
            }
            for d in schema.dmo_field_mappings
        ],
        "relationships": [
            {
                "source_dmo_name": r.source_dmo_name,
                "source_dmo_label": r.source_dmo_label,
                "source_field": r.source_field,
                "cardinality": r.cardinality,
                "related_entity": r.related_entity,
                "related_field": r.related_field,
                "relationship_label": r.relationship_label,
                "status": r.status,
            }
            for r in schema.relationships
        ],
    }


def from_dict(data: dict[str, Any]) -> OrgSchema:
    """Reconstruct an :class:`~models.OrgSchema` from a snapshot dict.

    The inverse of :func:`to_dict`. Field/object order is preserved as stored
    (the serializer wrote it already-sorted), so the round-trip is lossless.

    Args:
        data: A snapshot dict produced by :func:`to_dict`. A missing
            ``snapshot_version`` is assumed to be the current version.

    Raises:
        ValueError: If ``snapshot_version`` is newer than this build supports,
            rather than silently misreading a future format.
    """
    version = data.get("snapshot_version", SNAPSHOT_VERSION)
    if version != SNAPSHOT_VERSION:
        raise ValueError(
            f"Unsupported snapshot_version {version!r}; this build reads "
            f"version {SNAPSHOT_VERSION}. Upgrade data360-autodoc to read it."
        )
    return OrgSchema(
        org_name=data["org_name"],
        instance_url=data["instance_url"],
        generated_at=datetime.fromisoformat(data["generated_at"]),
        dmos=tuple(
            DataModelObject(name=o["name"], label=o["label"], fields=_fields_from(o))
            for o in data.get("dmos", [])
        ),
        dlos=tuple(
            DataLakeObject(name=o["name"], label=o["label"], fields=_fields_from(o))
            for o in data.get("dlos", [])
        ),
        cios=tuple(
            CalculatedInsight(
                name=c["name"],
                label=c["label"],
                dimensions=tuple(c.get("dimensions", [])),
                measures=tuple(c.get("measures", [])),
            )
            for c in data.get("cios", [])
        ),
        identity_rulesets=tuple(
            IdentityResolutionRuleset(
                name=r["name"],
                label=r["label"],
                match_rules=tuple(r.get("match_rules", [])),
                reconciliation_rule=r.get("reconciliation_rule"),
            )
            for r in data.get("identity_rulesets", [])
        ),
        mappings=tuple(
            Mapping(source_dlo=m["source_dlo"], target_dmo=m["target_dmo"])
            for m in data.get("mappings", [])
        ),
        streams=tuple(
            DataStream(
                name=s["name"],
                dlo_name=s["dlo_name"],
                dlo_label=s["dlo_label"],
                data_source=s.get("data_source"),
                category=s.get("category"),
                event_time_field=s.get("event_time_field"),
                primary_keys=tuple(s.get("primary_keys", [])),
                formula_fields=tuple(s.get("formula_fields", [])),
                formula_calculations=tuple(s.get("formula_calculations", [])),
                org_unit_identifier=s.get("org_unit_identifier"),
                schedule_frequency=s.get("schedule_frequency"),
                refresh_mode=s.get("refresh_mode"),
                de_extraction_mode=s.get("de_extraction_mode"),
            )
            for s in data.get("streams", [])
        ),
        field_mappings=tuple(
            FieldMapping(
                stream_name=fm["stream_name"],
                source_field=fm.get("source_field"),
                dlo_field_label=fm["dlo_field_label"],
                dlo_field_name=fm["dlo_field_name"],
                data_type=fm["data_type"],
                is_primary_key=fm.get("is_primary_key", False),
                is_foreign_key=fm.get("is_foreign_key", False),
                data_source=fm.get("data_source"),
                dlo_name=fm.get("dlo_name", ""),
                nullable=fm.get("nullable"),
            )
            for fm in data.get("field_mappings", [])
        ),
        dmo_field_mappings=tuple(
            DmoFieldMapping(
                source_dlo_name=d["source_dlo_name"],
                source_dlo_label=d["source_dlo_label"],
                source_field_name=d["source_field_name"],
                source_field_label=d["source_field_label"],
                target_dmo_name=d["target_dmo_name"],
                target_dmo_label=d["target_dmo_label"],
                target_field_name=d["target_field_name"],
                target_field_label=d["target_field_label"],
                data_source_field=d.get("data_source_field"),
                business_label=d.get("business_label"),
                manual_mapping=d.get("manual_mapping"),
            )
            for d in data.get("dmo_field_mappings", [])
        ),
        relationships=tuple(
            Relationship(
                source_dmo_name=r["source_dmo_name"],
                source_dmo_label=r["source_dmo_label"],
                source_field=r.get("source_field"),
                cardinality=r.get("cardinality"),
                related_entity=r.get("related_entity"),
                related_field=r.get("related_field"),
                relationship_label=r.get("relationship_label"),
                status=r.get("status"),
            )
            for r in data.get("relationships", [])
        ),
    )


def _object_to_dict(obj: DataModelObject | DataLakeObject) -> dict[str, Any]:
    """Serialize a DMO/DLO with its field list."""
    return {
        "name": obj.name,
        "label": obj.label,
        "fields": [
            {
                "name": f.name,
                "type": f.type,
                "is_key": f.is_key,
                "key_qualifier": f.key_qualifier,
                "type_inferred": f.type_inferred,
            }
            for f in obj.fields
        ],
    }


def _fields_from(obj: dict[str, Any]) -> tuple[FieldDef, ...]:
    """Rebuild a field tuple from a serialized DMO/DLO dict."""
    return tuple(
        FieldDef(
            name=f["name"],
            type=f["type"],
            is_key=f.get("is_key", False),
            key_qualifier=f.get("key_qualifier"),
            type_inferred=f.get("type_inferred", False),
        )
        for f in obj.get("fields", [])
    )
