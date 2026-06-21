"""Core data model for a Salesforce Data 360 org.

These dataclasses are the single source of truth that flows from the fetchers
(``fetcher/*``) into the document generators (``generator/*``). They are kept
deliberately framework-free so they can be serialized, diffed, and snapshot
tested.

The shapes here mirror the (currently mocked) API responses documented in
``agent_docs/api_reference.md``. When real org payloads become available, adjust
the ``from_api`` helpers rather than the consumers downstream.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class FieldDef:
    """A single field on a DMO or DLO.

    Attributes:
        name: API/developer name of the field.
        type: Data type as reported by the org (e.g. ``Text``, ``Number``).
        is_key: Whether the field participates in the object's primary key.
        key_qualifier: Optional key-qualifier label (DLO schema only); ``None``
            when the field is not a key or the API did not supply one.
    """

    name: str
    type: str
    is_key: bool = False
    key_qualifier: str | None = None

    @classmethod
    def from_api(cls, payload: dict[str, Any]) -> "FieldDef":
        """Build a :class:`FieldDef` from a raw metadata field object.

        Args:
            payload: A field entry from the metadata or DLO-schema response.

        Returns:
            A populated :class:`FieldDef`.
        """
        return cls(
            name=payload["name"],
            type=payload.get("type", "Unknown"),
            is_key=bool(payload.get("isKey", payload.get("keyQualifier"))),
            key_qualifier=payload.get("keyQualifier"),
        )


@dataclass(frozen=True)
class DataModelObject:
    """A Data Model Object (DMO)."""

    name: str
    label: str
    fields: tuple[FieldDef, ...] = ()

    @classmethod
    def from_api(cls, payload: dict[str, Any]) -> "DataModelObject":
        """Build a :class:`DataModelObject` from a raw metadata entity."""
        fields = tuple(
            sorted(
                (FieldDef.from_api(f) for f in payload.get("fields", [])),
                key=lambda fd: fd.name.lower(),
            )
        )
        return cls(
            name=payload["name"],
            label=payload.get("label", payload["name"]),
            fields=fields,
        )


@dataclass(frozen=True)
class DataLakeObject:
    """A Data Lake Object (DLO)."""

    name: str
    label: str
    fields: tuple[FieldDef, ...] = ()

    @classmethod
    def from_api(cls, payload: dict[str, Any]) -> "DataLakeObject":
        """Build a :class:`DataLakeObject` from a raw metadata entity."""
        fields = tuple(
            sorted(
                (FieldDef.from_api(f) for f in payload.get("fields", [])),
                key=lambda fd: fd.name.lower(),
            )
        )
        return cls(
            name=payload["name"],
            label=payload.get("label", payload["name"]),
            fields=fields,
        )


@dataclass(frozen=True)
class CalculatedInsight:
    """A Calculated Insight Object (CIO)."""

    name: str
    label: str
    dimensions: tuple[str, ...] = ()
    measures: tuple[str, ...] = ()

    @classmethod
    def from_api(cls, payload: dict[str, Any]) -> "CalculatedInsight":
        """Build a :class:`CalculatedInsight` from a raw metadata entity."""
        return cls(
            name=payload["name"],
            label=payload.get("label", payload["name"]),
            dimensions=tuple(sorted(payload.get("dimensions", []))),
            measures=tuple(sorted(payload.get("measures", []))),
        )


@dataclass(frozen=True)
class IdentityResolutionRuleset:
    """An Identity Resolution ruleset (match + reconciliation rules)."""

    name: str
    label: str
    match_rules: tuple[str, ...] = ()
    reconciliation_rule: str | None = None

    @classmethod
    def from_api(cls, payload: dict[str, Any]) -> "IdentityResolutionRuleset":
        """Build an :class:`IdentityResolutionRuleset` from raw metadata."""
        return cls(
            name=payload["name"],
            label=payload.get("label", payload["name"]),
            match_rules=tuple(sorted(payload.get("matchRules", []))),
            reconciliation_rule=payload.get("reconciliationRule"),
        )


@dataclass(frozen=True)
class Mapping:
    """A directed mapping from a source DLO to a target DMO."""

    source_dlo: str
    target_dmo: str

    @classmethod
    def from_api(cls, payload: dict[str, Any]) -> "Mapping":
        """Build a :class:`Mapping` from a raw metadata mapping entry."""
        return cls(source_dlo=payload["sourceDlo"], target_dmo=payload["targetDmo"])


@dataclass
class OrgSchema:
    """Normalized snapshot of everything we document for one Data 360 org.

    Collections are sorted alphabetically so that the same org always produces
    byte-identical output (a project-wide determinism guarantee).
    """

    org_name: str
    instance_url: str
    generated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    dmos: tuple[DataModelObject, ...] = ()
    dlos: tuple[DataLakeObject, ...] = ()
    cios: tuple[CalculatedInsight, ...] = ()
    identity_rulesets: tuple[IdentityResolutionRuleset, ...] = ()
    mappings: tuple[Mapping, ...] = ()

    @classmethod
    def from_metadata(
        cls,
        payload: dict[str, Any],
        *,
        instance_url: str,
        org_name: str | None = None,
        generated_at: datetime | None = None,
    ) -> "OrgSchema":
        """Normalize a raw ``/api/v1/metadata/`` response into an OrgSchema.

        Args:
            payload: The aggregated metadata response (all pages merged), with
                ``dmos``, ``dlos``, ``cios``, ``identityResolutionRulesets`` and
                ``mappings`` keys.
            instance_url: The org's instance URL.
            org_name: Human-readable org name for the document title. Falls back
                to ``payload['orgName']`` and then the instance host.
            generated_at: Override timestamp (mainly for deterministic tests).

        Returns:
            A fully populated, alphabetically sorted :class:`OrgSchema`.
        """
        resolved_name = (
            org_name
            or payload.get("orgName")
            or instance_url.split("//", 1)[-1].split("/", 1)[0]
        )
        dmos = tuple(
            sorted(
                (DataModelObject.from_api(d) for d in payload.get("dmos", [])),
                key=lambda o: o.name.lower(),
            )
        )
        dlos = tuple(
            sorted(
                (DataLakeObject.from_api(d) for d in payload.get("dlos", [])),
                key=lambda o: o.name.lower(),
            )
        )
        cios = tuple(
            sorted(
                (CalculatedInsight.from_api(c) for c in payload.get("cios", [])),
                key=lambda o: o.name.lower(),
            )
        )
        rulesets = tuple(
            sorted(
                (
                    IdentityResolutionRuleset.from_api(r)
                    for r in payload.get("identityResolutionRulesets", [])
                ),
                key=lambda o: o.name.lower(),
            )
        )
        mappings = tuple(
            sorted(
                (Mapping.from_api(m) for m in payload.get("mappings", [])),
                key=lambda m: (m.source_dlo.lower(), m.target_dmo.lower()),
            )
        )
        kwargs: dict[str, Any] = dict(
            org_name=resolved_name,
            instance_url=instance_url,
            dmos=dmos,
            dlos=dlos,
            cios=cios,
            identity_rulesets=rulesets,
            mappings=mappings,
        )
        if generated_at is not None:
            kwargs["generated_at"] = generated_at
        return cls(**kwargs)
