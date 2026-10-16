"""Schema drift detection: compare two :class:`~models.OrgSchema` snapshots.

Pure function of two snapshots -> :class:`SchemaDiff`. This is the payoff of
the deterministic JSON snapshot: save one today, fetch again next week (or from
another org — sandbox vs production), and :func:`diff_schemas` reports exactly
what changed.

What is compared, and how each item is identified:

- **DMOs / DLOs** — by API name. Added / removed objects, label changes, and
  per-field drift (added / removed fields; ``type``, ``is_key`` and
  ``key_qualifier`` changes).
- **DLO → DMO object mappings** — by ``(source_dlo, target_dmo)``.
- **DLO → DMO field mappings** — by ``(source DLO, source field, target DMO,
  target field)``. A field re-pointed to another attribute shows up as one
  removed plus one added mapping.
- **DMO relationships** — by ``(source DMO, source field, related object,
  related field)``; ``cardinality``, ``status`` and ``relationship_label``
  changes are reported as changed.

Deliberately ignored: ``generated_at`` (always differs), display labels on
mapping rows (cosmetic), and ``FieldDef.type_inferred`` (type *provenance*,
not a schema change — a resolved type that changes still shows up as a
``type`` change).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Hashable, Iterable, TypeVar

from data360_autodoc.models import (
    DataLakeObject,
    DataModelObject,
    DmoFieldMapping,
    FieldDef,
    Mapping,
    OrgSchema,
    Relationship,
)

#: Field attributes compared for drift (``type_inferred`` is provenance only).
FIELD_ATTRIBUTES = ("type", "is_key", "key_qualifier")

#: Relationship attributes compared for drift (the rest form its identity).
RELATIONSHIP_ATTRIBUTES = ("cardinality", "status", "relationship_label")

T = TypeVar("T")


@dataclass(frozen=True)
class ValueChange:
    """One attribute that differs between the old and new snapshot."""

    attribute: str
    old: Any
    new: Any


@dataclass(frozen=True)
class FieldChange:
    """A field present in both snapshots whose attributes changed."""

    name: str
    changes: tuple[ValueChange, ...]


@dataclass(frozen=True)
class ObjectChange:
    """A DMO/DLO present in both snapshots that changed (label or fields)."""

    name: str
    label: str
    changes: tuple[ValueChange, ...] = ()
    added_fields: tuple[FieldDef, ...] = ()
    removed_fields: tuple[FieldDef, ...] = ()
    changed_fields: tuple[FieldChange, ...] = ()


@dataclass(frozen=True)
class ObjectDiff:
    """Added / removed / changed DMOs or DLOs."""

    added: tuple[DataModelObject | DataLakeObject, ...] = ()
    removed: tuple[DataModelObject | DataLakeObject, ...] = ()
    changed: tuple[ObjectChange, ...] = ()

    def field_counts(self) -> dict[str, int]:
        """Field-level counts across the objects present in both snapshots."""
        return {
            "added": sum(len(c.added_fields) for c in self.changed),
            "removed": sum(len(c.removed_fields) for c in self.changed),
            "changed": sum(len(c.changed_fields) for c in self.changed),
        }


@dataclass(frozen=True)
class RelationshipChange:
    """A relationship present in both snapshots whose attributes changed."""

    relationship: Relationship
    changes: tuple[ValueChange, ...]


@dataclass(frozen=True)
class SnapshotInfo:
    """Header of one compared snapshot (which org, when)."""

    org_name: str
    instance_url: str
    generated_at: datetime


@dataclass(frozen=True)
class SchemaDiff:
    """Everything that differs between two org snapshots."""

    old: SnapshotInfo
    new: SnapshotInfo
    dmos: ObjectDiff = field(default_factory=ObjectDiff)
    dlos: ObjectDiff = field(default_factory=ObjectDiff)
    mappings_added: tuple[Mapping, ...] = ()
    mappings_removed: tuple[Mapping, ...] = ()
    field_mappings_added: tuple[DmoFieldMapping, ...] = ()
    field_mappings_removed: tuple[DmoFieldMapping, ...] = ()
    relationships_added: tuple[Relationship, ...] = ()
    relationships_removed: tuple[Relationship, ...] = ()
    relationships_changed: tuple[RelationshipChange, ...] = ()

    def summary(self) -> dict[str, dict[str, int]]:
        """Per-area ``added`` / ``removed`` / ``changed`` counts.

        Field counts cover objects present in both snapshots; the fields of an
        added or removed object are implied by the object itself.
        """
        return {
            "dmos": _counts(self.dmos.added, self.dmos.removed, self.dmos.changed),
            "dmo_fields": self.dmos.field_counts(),
            "dlos": _counts(self.dlos.added, self.dlos.removed, self.dlos.changed),
            "dlo_fields": self.dlos.field_counts(),
            "mappings": _counts(self.mappings_added, self.mappings_removed),
            "field_mappings": _counts(
                self.field_mappings_added, self.field_mappings_removed
            ),
            "relationships": _counts(
                self.relationships_added,
                self.relationships_removed,
                self.relationships_changed,
            ),
        }

    @property
    def change_count(self) -> int:
        """Total number of individual changes.

        A "changed" DMO/DLO is a container, not a change of its own: it counts
        through its label change and field-level changes, so one retyped field
        is one change, not two.
        """
        total = 0
        for area, counts in self.summary().items():
            total += counts["added"] + counts["removed"]
            if area not in ("dmos", "dlos"):
                total += counts["changed"]
        for objects in (self.dmos, self.dlos):
            total += sum(len(c.changes) for c in objects.changed)
        return total

    @property
    def has_changes(self) -> bool:
        """True when the two snapshots differ in any compared area."""
        return self.change_count > 0


def diff_schemas(old: OrgSchema, new: OrgSchema) -> SchemaDiff:
    """Compare two org snapshots and return what changed from ``old`` to ``new``.

    Deterministic: every collection in the result is sorted case-insensitively
    by its identity, independent of the input order.
    """
    mappings_added, mappings_removed = _added_removed(
        old.mappings,
        new.mappings,
        key=lambda m: (m.source_dlo, m.target_dmo),
    )
    fm_added, fm_removed = _added_removed(
        old.dmo_field_mappings,
        new.dmo_field_mappings,
        key=_field_mapping_key,
    )
    return SchemaDiff(
        old=_info(old),
        new=_info(new),
        dmos=_diff_objects(old.dmos, new.dmos),
        dlos=_diff_objects(old.dlos, new.dlos),
        mappings_added=mappings_added,
        mappings_removed=mappings_removed,
        field_mappings_added=fm_added,
        field_mappings_removed=fm_removed,
        **_diff_relationships(old.relationships, new.relationships),
    )


def _info(schema: OrgSchema) -> SnapshotInfo:
    return SnapshotInfo(
        org_name=schema.org_name,
        instance_url=schema.instance_url,
        generated_at=schema.generated_at,
    )


def _counts(added: tuple, removed: tuple, changed: tuple = ()) -> dict[str, int]:
    return {"added": len(added), "removed": len(removed), "changed": len(changed)}


def _sort_key(key: Any) -> tuple[str, ...]:
    """Case-insensitive sort key for a str or tuple-of-optional-str identity."""
    parts = key if isinstance(key, tuple) else (key,)
    return tuple((p or "").lower() for p in parts)


def _by_name(item: Any) -> str:
    return item.name.lower()


def _index(items: Iterable[T], key: Callable[[T], Hashable]) -> dict[Hashable, T]:
    return {key(item): item for item in items}


def _added_removed(
    old: Iterable[T], new: Iterable[T], key: Callable[[T], Hashable]
) -> tuple[tuple[T, ...], tuple[T, ...]]:
    """Items only in ``new`` (added) and only in ``old`` (removed), sorted."""
    old_by_key, new_by_key = _index(old, key), _index(new, key)
    added = [new_by_key[k] for k in new_by_key.keys() - old_by_key.keys()]
    removed = [old_by_key[k] for k in old_by_key.keys() - new_by_key.keys()]
    return (
        tuple(sorted(added, key=lambda i: _sort_key(key(i)))),
        tuple(sorted(removed, key=lambda i: _sort_key(key(i)))),
    )


def _value_changes(old: Any, new: Any, attributes: tuple[str, ...]) -> tuple:
    return tuple(
        ValueChange(attribute=a, old=getattr(old, a), new=getattr(new, a))
        for a in attributes
        if getattr(old, a) != getattr(new, a)
    )


def _diff_objects(
    old: tuple[DataModelObject | DataLakeObject, ...],
    new: tuple[DataModelObject | DataLakeObject, ...],
) -> ObjectDiff:
    """Diff DMOs or DLOs by API name, descending into their fields."""
    added, removed = _added_removed(old, new, key=lambda o: o.name)
    old_by_name = _index(old, lambda o: o.name)
    changed: list[ObjectChange] = []
    for new_obj in sorted(_index(new, lambda o: o.name).values(), key=_by_name):
        old_obj = old_by_name.get(new_obj.name)
        if old_obj is None:
            continue
        fields_added, fields_removed = _added_removed(
            old_obj.fields, new_obj.fields, key=lambda f: f.name
        )
        old_fields = _index(old_obj.fields, lambda f: f.name)
        fields_changed = tuple(
            FieldChange(name=f.name, changes=changes)
            for f in sorted(
                _index(new_obj.fields, lambda f: f.name).values(), key=_by_name
            )
            if f.name in old_fields
            and (changes := _value_changes(old_fields[f.name], f, FIELD_ATTRIBUTES))
        )
        label_changes = _value_changes(old_obj, new_obj, ("label",))
        if label_changes or fields_added or fields_removed or fields_changed:
            changed.append(
                ObjectChange(
                    name=new_obj.name,
                    label=new_obj.label,
                    changes=label_changes,
                    added_fields=fields_added,
                    removed_fields=fields_removed,
                    changed_fields=fields_changed,
                )
            )
    return ObjectDiff(added=added, removed=removed, changed=tuple(changed))


def _field_mapping_key(m: DmoFieldMapping) -> tuple[str, str, str, str]:
    return (
        m.source_dlo_name,
        m.source_field_name,
        m.target_dmo_name,
        m.target_field_name,
    )


def _relationship_key(r: Relationship) -> tuple[str | None, ...]:
    return (r.source_dmo_name, r.source_field, r.related_entity, r.related_field)


def _diff_relationships(
    old: tuple[Relationship, ...], new: tuple[Relationship, ...]
) -> dict[str, tuple]:
    added, removed = _added_removed(old, new, key=_relationship_key)
    old_by_key = _index(old, _relationship_key)
    new_by_key = _index(new, _relationship_key)
    changed = tuple(
        RelationshipChange(relationship=r, changes=changes)
        for r in sorted(
            new_by_key.values(), key=lambda r: _sort_key(_relationship_key(r))
        )
        if _relationship_key(r) in old_by_key
        and (
            changes := _value_changes(
                old_by_key[_relationship_key(r)], r, RELATIONSHIP_ATTRIBUTES
            )
        )
    )
    return {
        "relationships_added": added,
        "relationships_removed": removed,
        "relationships_changed": changed,
    }
