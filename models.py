"""Core data model for a Salesforce Data 360 org.

These dataclasses are the single source of truth that flows from the fetchers
(``fetcher/*``) into the document generators (``generator/*``). They are kept
deliberately framework-free so they can be serialized, diffed, and snapshot
tested.

Construction lives in the fetchers (which know the real Data 360 Connect REST
API shapes — see ``agent_docs/api_reference.md``); the only assembly helper here
is :meth:`OrgSchema.build`, which sorts every collection so the same org always
produces byte-identical output (the project's determinism guarantee).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class FieldDef:
    """A single field on a DMO or DLO.

    Attributes:
        name: API/developer name of the field.
        type: Data type as reported by the org (e.g. ``Text``, ``Number``).
        is_key: Whether the field participates in the object's primary key.
        key_qualifier: Optional key-qualifier label; ``None`` when the field is
            not a key or the API did not supply one.
    """

    name: str
    type: str
    is_key: bool = False
    key_qualifier: str | None = None
    #: True when ``type`` was resolved from the mapped DLO field (the DMO
    #: endpoint returned a generic/Unknown type). The type token stays clean;
    #: renderers surface the provenance (e.g. a "(via DLO)" marker), not this.
    type_inferred: bool = False


@dataclass(frozen=True)
class DataModelObject:
    """A Data Model Object (DMO)."""

    name: str
    label: str
    fields: tuple[FieldDef, ...] = ()


@dataclass(frozen=True)
class DataLakeObject:
    """A Data Lake Object (DLO)."""

    name: str
    label: str
    fields: tuple[FieldDef, ...] = ()


@dataclass(frozen=True)
class DataStream:
    """One Data Stream and its source/refresh metadata (the SI doc's Sheet 1).

    Lightweight, table-oriented row that sits alongside the DLOs. ``dlo_name`` /
    ``dlo_label`` link the row to the DLO it populates. Scalar fields are
    ``None`` when the org's JSON did not supply them.
    """

    name: str
    dlo_name: str
    dlo_label: str
    data_source: str | None = None
    category: str | None = None
    event_time_field: str | None = None
    primary_keys: tuple[str, ...] = ()
    formula_fields: tuple[str, ...] = ()
    formula_calculations: tuple[str, ...] = ()
    org_unit_identifier: str | None = None
    schedule_frequency: str | None = None
    refresh_mode: str | None = None
    de_extraction_mode: str | None = None


@dataclass(frozen=True)
class FieldMapping:
    """One Source → DLO field-mapping row (the SI doc's Sheet 2).

    ``source_field`` is the original source field name (``None`` for Data Cloud
    system fields with no source). ``is_foreign_key`` is heuristic — true for
    fields whose API name starts with ``KQ_`` (Key Qualifier). Nullability is not
    exposed by ``/ssot/data-streams`` and is therefore not modeled.
    """

    stream_name: str
    source_field: str | None
    dlo_field_label: str
    dlo_field_name: str
    data_type: str
    is_primary_key: bool = False
    is_foreign_key: bool = False
    data_source: str | None = None
    #: DLO API name this field belongs to (e.g. ``Account_CRM__dll``).
    dlo_name: str = ""
    #: Tri-state nullability: ``True``/``False`` when the source exposes it,
    #: ``None`` when unknown (``/ssot/data-streams`` does not expose nullability,
    #: so this is ``None`` for those streams — rendered blank, never guessed).
    nullable: bool | None = None


@dataclass(frozen=True)
class CalculatedInsight:
    """A Calculated Insight Object (CIO)."""

    name: str
    label: str
    dimensions: tuple[str, ...] = ()
    measures: tuple[str, ...] = ()


@dataclass(frozen=True)
class IdentityResolutionRuleset:
    """An Identity Resolution ruleset (match + reconciliation rules)."""

    name: str
    label: str
    match_rules: tuple[str, ...] = ()
    reconciliation_rule: str | None = None


@dataclass(frozen=True)
class Mapping:
    """A directed mapping from a source DLO to a target DMO."""

    source_dlo: str
    target_dmo: str


@dataclass(frozen=True)
class DmoFieldMapping:
    """One DLO→DMO field-level mapping row (the SI doc's Sheet 3).

    Carries all eight columns of the verified Apex export. Field-level labels
    fall back to their API name when the API exposes no human label (Data Cloud
    ``__dll``/``__dlm`` objects are not describable, so ``Schema.describe`` —
    the Apex label source — fails for them).
    """

    source_dlo_name: str
    source_dlo_label: str
    source_field_name: str
    source_field_label: str
    target_dmo_name: str
    target_dmo_label: str
    target_field_name: str
    target_field_label: str
    #: Underlying source-system field reference, when the mapping/connector
    #: payload exposes one; ``None`` otherwise (kept blank, never fabricated).
    data_source_field: str | None = None
    #: Manual/glossary columns — not derivable from metadata. Always ``None``
    #: here; present so the sheet structure has a place to hold curated values.
    business_label: str | None = None
    manual_mapping: str | None = None


@dataclass(frozen=True)
class Relationship:
    """A DMO relationship row (the SI doc's Relationships sheet / Sheet 8).

    Built from ``/ssot/data-model-objects/{dmo}/relationships``. ``source_dmo_*``
    is the DMO that was queried (authoritative). The related entity/field and
    cardinality are read defensively from the payload across known Data Cloud
    key spellings; any property the org does not expose is left ``None`` and
    rendered blank — the row is never dropped just because a column is empty.
    """

    source_dmo_name: str
    source_dmo_label: str
    source_field: str | None = None
    cardinality: str | None = None
    related_entity: str | None = None
    related_field: str | None = None
    relationship_label: str | None = None
    #: Relationship status as reported by the API (ACTIVE / INACTIVE /
    #: DEACTIVATEDBYUSER / …). Surfaced so inactive standard relationships are
    #: visible and filterable rather than silently dropped.
    status: str | None = None


@dataclass
class OrgSchema:
    """Normalized snapshot of everything we document for one Data 360 org."""

    org_name: str
    instance_url: str
    generated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    dmos: tuple[DataModelObject, ...] = ()
    dlos: tuple[DataLakeObject, ...] = ()
    cios: tuple[CalculatedInsight, ...] = ()
    identity_rulesets: tuple[IdentityResolutionRuleset, ...] = ()
    mappings: tuple[Mapping, ...] = ()
    streams: tuple[DataStream, ...] = ()
    field_mappings: tuple[FieldMapping, ...] = ()
    dmo_field_mappings: tuple[DmoFieldMapping, ...] = ()
    relationships: tuple[Relationship, ...] = ()

    @classmethod
    def build(
        cls,
        *,
        org_name: str,
        instance_url: str,
        dmos: tuple[DataModelObject, ...] = (),
        dlos: tuple[DataLakeObject, ...] = (),
        cios: tuple[CalculatedInsight, ...] = (),
        identity_rulesets: tuple[IdentityResolutionRuleset, ...] = (),
        mappings: tuple[Mapping, ...] = (),
        streams: tuple[DataStream, ...] = (),
        field_mappings: tuple[FieldMapping, ...] = (),
        dmo_field_mappings: tuple[DmoFieldMapping, ...] = (),
        relationships: tuple[Relationship, ...] = (),
        generated_at: datetime | None = None,
    ) -> "OrgSchema":
        """Assemble an :class:`OrgSchema`, sorting every collection.

        Sorting (objects by name, mappings by (source, target)) is what makes
        the downstream document output deterministic. Field-level sorting is the
        fetcher's job, done as each object is constructed.
        """
        kwargs = dict(
            org_name=org_name,
            instance_url=instance_url,
            dmos=tuple(sorted(dmos, key=lambda o: o.name.lower())),
            dlos=tuple(sorted(dlos, key=lambda o: o.name.lower())),
            cios=tuple(sorted(cios, key=lambda o: o.name.lower())),
            identity_rulesets=tuple(
                sorted(identity_rulesets, key=lambda o: o.name.lower())
            ),
            mappings=tuple(
                sorted(
                    mappings,
                    key=lambda m: (m.source_dlo.lower(), m.target_dmo.lower()),
                )
            ),
            streams=tuple(sorted(streams, key=lambda s: s.name.lower())),
            field_mappings=tuple(
                sorted(
                    field_mappings,
                    key=lambda fm: (
                        fm.stream_name.lower(),
                        fm.dlo_field_name.lower(),
                    ),
                )
            ),
            dmo_field_mappings=tuple(
                sorted(
                    dmo_field_mappings,
                    key=lambda dfm: (
                        dfm.source_dlo_name.lower(),
                        dfm.target_dmo_name.lower(),
                        dfm.source_field_name.lower(),
                    ),
                )
            ),
            relationships=tuple(
                sorted(
                    relationships,
                    key=lambda r: (
                        r.source_dmo_name.lower(),
                        (r.source_field or "").lower(),
                        (r.related_entity or "").lower(),
                    ),
                )
            ),
        )
        if generated_at is not None:
            kwargs["generated_at"] = generated_at
        return cls(**kwargs)
