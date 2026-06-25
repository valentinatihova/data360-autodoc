"""Data 360 metadata orchestrator.

The real Data 360 Connect REST API has no single metadata endpoint — the org
schema is assembled from several ``/ssot/*`` calls (verified against a live org;
see ``agent_docs/api_reference.md``):

    DMOs            GET /ssot/data-model-objects?limit=500
    DLO→DMO maps    GET /ssot/data-model-object-mappings?dataspace=..&dmoDeveloperName=..
    DLOs + fields   GET /ssot/data-streams           (delegated to streams.py)

``fetch_metadata`` runs these, derives each DMO's documented fields from the
mapping target fields, and assembles a sorted :class:`~models.OrgSchema`.

Calculated Insights and Identity Resolution rulesets are not yet wired — no
endpoint for them is verified against a real org, so they come back empty.
"""

from __future__ import annotations

import logging
from dataclasses import replace
from typing import Any, Callable, Final

from fetcher._http import FetchError, get_json, iter_pages
from models import (
    DataModelObject,
    DmoFieldMapping,
    FieldDef,
    FieldMapping,
    Mapping,
    OrgSchema,
    Relationship,
)
from fetcher.streams import StreamsError, fetch_dlos_and_streams

#: DMO field types that carry no real type information; safe to override with a
#: type inferred from the mapped DLO field (see :func:`_enrich_dmo_field_types`).
_GENERIC_DMO_TYPES: Final = frozenset(
    {"", "unknown", "mktdatamodelfield", "mktcalculatedinsightfield"}
)

logger = logging.getLogger(__name__)

#: Optional progress callback: ``(message, inline)``. ``inline=True`` updates the
#: current line in place (a live counter); ``inline=False`` is a status line.
ProgressFn = Callable[[str, bool], None]

#: Default Data API version (verified working against a live org).
DEFAULT_API_VERSION: Final = "v62.0"
#: Default Data Cloud dataspace.
DEFAULT_DATASPACE: Final = "default"
#: Safety cap on DMOs processed (each costs a mappings + relationships call).
_MAX_DMOS: Final = 500


class MetadataError(RuntimeError):
    """Raised when the org metadata cannot be retrieved."""


def detect_api_version(
    *,
    instance_url: str,
    access_token: str,
    timeout: float = 30.0,
    fallback: str = DEFAULT_API_VERSION,
) -> str:
    """Return the org's highest available Data API version (e.g. ``v66.0``).

    Queries ``GET /services/data/``, which returns the list of versions the org
    supports, and picks the numerically highest. Different ``/ssot/*`` endpoints
    require different minimum versions (``data-model-objects`` needs a recent
    one), so detecting the org's max avoids hardcoding a guess that 404s.

    Falls back to ``fallback`` if discovery fails or returns nothing — a
    stale-but-usable floor beats crashing.
    """
    base = instance_url.rstrip("/")
    try:
        data = get_json(
            f"{base}/services/data/", access_token=access_token, timeout=timeout
        )
    except FetchError:
        return fallback

    best: float | None = None
    best_str: str | None = None
    for entry in data if isinstance(data, list) else []:
        if not isinstance(entry, dict):
            continue
        raw = entry.get("version")
        try:
            num = float(raw)
        except (TypeError, ValueError):
            continue
        if best is None or num > best:
            best, best_str = num, str(raw)
    return f"v{best_str}" if best_str else fallback


def fetch_metadata(
    *,
    instance_url: str,
    access_token: str,
    api_version: str | None = None,
    dataspace: str = DEFAULT_DATASPACE,
    org_name: str | None = None,
    timeout: float = 60.0,
    progress: ProgressFn | None = None,
) -> OrgSchema:
    """Fetch and normalize the full org schema from the Connect REST API.

    Args:
        instance_url: Org base URL.
        access_token: OAuth bearer token from :func:`fetcher.auth.get_access_token`.
        api_version: Data API version (e.g. ``v62.0``). When ``None`` (default),
            the org's highest version is auto-detected via
            :func:`detect_api_version`.
        dataspace: Data Cloud dataspace name.
        org_name: Optional document-title override; defaults to the instance host.
        timeout: Per-request timeout in seconds.

    Returns:
        A sorted :class:`~models.OrgSchema`.

    Raises:
        MetadataError: If any required request fails.
    """
    base = instance_url.rstrip("/")
    resolved_name = org_name or base.split("//", 1)[-1].split("/", 1)[0]

    if api_version is None:
        api_version = detect_api_version(
            instance_url=instance_url, access_token=access_token, timeout=timeout
        )
    if progress:
        progress(f"Using API version {api_version}", False)

    try:
        dmo_entries = _fetch_dmo_list(base, api_version, access_token, timeout)
        if progress:
            progress(f"Found {len(dmo_entries)} DMO(s); fetching metadata…", False)
        dmos, mappings, dmo_field_mappings, relationships, skipped = _fetch_dmo_details(
            base, api_version, dataspace, dmo_entries, access_token, timeout, progress
        )
        if progress:
            progress("Fetching data streams…", False)
        dlos, streams, field_mappings = fetch_dlos_and_streams(
            instance_url=instance_url,
            access_token=access_token,
            api_version=api_version,
            timeout=timeout,
        )
        # DLO field metadata only becomes available after the streams fetch, so
        # enrich here: real source-field labels + DLO-inferred DMO field types.
        # The DLO field index is built once and shared by both enrich passes.
        dlo_field_labels, dlo_field_types = _dlo_field_index(field_mappings)
        dlo_obj_label = {s.dlo_name: s.dlo_label for s in streams if s.dlo_name}
        dmo_field_mappings = _enrich_dmo_field_mappings(
            dmo_field_mappings, dlo_obj_label, dlo_field_labels
        )
        dmos = _enrich_dmo_field_types(dmos, dmo_field_mappings, dlo_field_types)
    except (FetchError, StreamsError) as exc:
        # Single funnel for FATAL fetches (DMO list, DLO/streams): these become a
        # MetadataError the CLI renders cleanly. Per-DMO mapping/relationship
        # failures are NOT fatal — _fetch_dmo_details skips those DMOs instead.
        raise MetadataError(str(exc)) from exc

    if skipped:
        logger.warning(
            "Skipped %d of %d DMO(s) due to fetch errors: %s",
            len(skipped),
            len(dmo_entries),
            ", ".join(skipped),
        )

    return OrgSchema.build(
        org_name=resolved_name,
        instance_url=instance_url,
        dmos=tuple(dmos),
        dlos=dlos,
        mappings=tuple(mappings),
        streams=streams,
        field_mappings=field_mappings,
        dmo_field_mappings=tuple(dmo_field_mappings),
        relationships=tuple(relationships),
    )


def _fetch_dmo_list(
    base: str, api_version: str, access_token: str, timeout: float
) -> list[tuple[str, str]]:
    """Return ``(name, label)`` for every enabled DMO.

    Capped at :data:`_MAX_DMOS`; logs a WARNING (so the omission is never silent)
    if the org has more enabled DMOs than the cap.
    """
    url = f"{base}/services/data/{api_version}/ssot/data-model-objects?limit=500"
    out: list[tuple[str, str]] = []
    truncated = False
    for page in iter_pages(
        url, base_url=base, access_token=access_token, timeout=timeout
    ):
        for entry in page.get("dataModelObject", []):
            if entry.get("isEnabled") is False:
                continue
            name = entry.get("name")
            if not name:
                continue
            if len(out) >= _MAX_DMOS:
                # A valid DMO exists beyond the cap -> genuine truncation.
                truncated = True
                break
            out.append((name, entry.get("label") or name))
        if truncated:
            break
    if truncated:
        logger.warning(
            "DMO list capped at %d; some DMOs were omitted from the document.",
            _MAX_DMOS,
        )
    return out


# Verified shape of one relationship (live org, v67.0 — see
# agent_docs/api_reference.md). Each side is a nested object:
#   {"cardinality": "ManyToOne", "status": "INACTIVE", "name": "<rel name>",
#    "sourceObject": {"name": "ssot__Account__dlm", "label": "Account"},
#    "sourceField":  {"name": "ssot__…Id__c", "type": "MktDataModelField"},
#    "targetObject": {"name": "ssot__ContactPointEmail__dlm", "label": "…"},
#    "targetField":  {"name": "ssot__Id__c", "type": "MktDataModelField"}}
# The queried DMO may be EITHER side. Scalar *_KEYS are kept only as a fallback
# for any org/version that flattens the objects; values are only read, never
# invented.
_REL_SRC_FIELD_KEYS: Final = ("sourceFieldDeveloperName", "fromEntityAttribute")
_REL_TGT_FIELD_KEYS: Final = (
    "targetFieldDeveloperName",
    "toEntityAttribute",
    "relatedFieldDeveloperName",
)
_REL_SRC_ENTITY_KEYS: Final = ("sourceEntityDeveloperName", "fromEntity")
_REL_TGT_ENTITY_KEYS: Final = (
    "targetEntityDeveloperName",
    "toEntity",
    "relatedEntityDeveloperName",
    "relatedEntity",
)
#: Cardinality code -> compact notation. Input is upper-cased + stripped first,
#: so "ManyToOne", "MANY_TO_ONE", etc. all normalize.
_CARDINALITY: Final = {
    "ONETOONE": "1:1",
    "MANYTOONE": "N:1",
    "ONETOMANY": "1:N",
    "MANYTOMANY": "N:N",
}


def _fetch_dmo_relationships(
    base: str,
    api_version: str,
    dataspace: str,
    dmo_name: str,
    access_token: str,
    timeout: float,
) -> tuple[dict[str, FieldDef], list[Relationship]]:
    """Fetch a DMO's relationships, returning ``(fields, relationships)``.

    The relationships response is used for two things:

    - **Field types:** the side that *is* the queried DMO contributes a ``name``/
      ``type`` field (these are typically generic ``MktDataModelField`` types in
      practice, so DLO inference is the real type source — see
      :func:`_enrich_dmo_field_types`).
    - **Relationship rows:** ``sourceObject``/``targetObject`` describe both ends
      explicitly, so a row is built straight from the payload. Inactive rows are
      kept (with their status) so standard relationships are visible, not
      silently dropped; fields used for type extraction stay ACTIVE-only.

    Fields are de-duplicated by name.
    """
    url = (
        f"{base}/services/data/{api_version}/ssot/data-model-objects/"
        f"{dmo_name}/relationships?dataspace={dataspace}&limit=500"
    )
    fields: dict[str, FieldDef] = {}
    relationships: list[Relationship] = []
    for page in iter_pages(
        url, base_url=base, access_token=access_token, timeout=timeout
    ):
        for rel in page.get("relationships", []):
            if not isinstance(rel, dict):
                continue
            field, relationship = _parse_relationship(rel, dmo_name)
            status = rel.get("status")
            is_active = not status or status == "ACTIVE"
            if field and is_active and field.name not in fields:
                fields[field.name] = field
            if relationship is not None:
                relationships.append(relationship)
    return fields, relationships


def _parse_relationship(
    rel: dict[str, Any], queried_dmo_name: str
) -> tuple[FieldDef | None, Relationship | None]:
    """Parse one relationship dict into ``(field, relationship)``.

    Pure and side-effect-free so it is unit-testable. The payload is
    self-describing via ``sourceObject``/``targetObject``; the queried DMO may be
    either side, so ``field`` (for DMO field-type extraction) is taken from
    whichever side IS the queried DMO. ``relationship`` is ``None`` only when the
    dict carries no relationship information at all. Scalar ``*_KEYS`` are a
    fallback for any flattened variant; the nested objects are the verified shape.
    """
    source_obj = rel.get("sourceObject") or {}
    source_name = _dict_or_str_name(rel, "sourceObject", _REL_SRC_ENTITY_KEYS)
    target_name = _dict_or_str_name(rel, "targetObject", _REL_TGT_ENTITY_KEYS)
    source_label = source_obj.get("label") if isinstance(source_obj, dict) else None
    source_field = _dict_or_str_name(rel, "sourceField", _REL_SRC_FIELD_KEYS)
    target_field = _dict_or_str_name(rel, "targetField", _REL_TGT_FIELD_KEYS)
    cardinality = _cardinality(rel.get("cardinality"))
    status = rel.get("status")
    label = rel.get("name") if isinstance(rel.get("name"), str) else None

    # Field-type extraction: take the side that IS the queried DMO (the payload
    # field belongs to its own object, not necessarily the one we queried).
    field: FieldDef | None = None
    if source_name == queried_dmo_name:
        field = _field_from(rel.get("sourceField"))
    elif target_name == queried_dmo_name:
        field = _field_from(rel.get("targetField"))
    elif source_name is None and target_name is None:
        # No object attribution in the payload: the endpoint is scoped to the
        # queried DMO, so attribute its sourceField to it (defensive fallback).
        field = _field_from(rel.get("sourceField"))

    relationship: Relationship | None = None
    if any((source_name, source_field, target_name, target_field, cardinality)):
        relationship = Relationship(
            source_dmo_name=source_name or queried_dmo_name,
            source_dmo_label=source_label or source_name or queried_dmo_name,
            source_field=source_field,
            cardinality=cardinality,
            related_entity=target_name,
            related_field=target_field,
            relationship_label=label,
            status=status,
        )
    return field, relationship


def _field_from(fld: Any) -> FieldDef | None:
    """Build a FieldDef from a relationship ``{name, type}`` dict, if present."""
    if isinstance(fld, dict) and isinstance(fld.get("name"), str) and fld["name"]:
        return FieldDef(name=fld["name"], type=fld.get("type") or "Unknown")
    return None


def _first_str(d: dict[str, Any], keys: tuple[str, ...]) -> str | None:
    """First non-empty string value among ``keys``, else ``None``."""
    for k in keys:
        v = d.get(k)
        if isinstance(v, str) and v:
            return v
    return None


def _dict_or_str_name(
    rel: dict[str, Any], dict_key: str, scalar_keys: tuple[str, ...]
) -> str | None:
    """``name`` from a nested ``{name: …}`` object/field, else scalar fallback."""
    obj = rel.get(dict_key)
    if isinstance(obj, dict):
        name = obj.get("name")
        if isinstance(name, str) and name:
            return name
    return _first_str(rel, scalar_keys)


def _cardinality(raw: Any) -> str | None:
    """Normalize a cardinality code (e.g. ``MANYTOONE`` -> ``N:1``)."""
    if not raw:
        return None
    key = str(raw).upper().replace("_", "").replace("-", "").replace(" ", "")
    return _CARDINALITY.get(key, str(raw))


def _merge_dmo_fields(
    typed: dict[str, FieldDef], mapping_fields: list[FieldDef]
) -> tuple[FieldDef, ...]:
    """Merge relationship-typed fields with mapping-derived names, sorted.

    Relationship fields (real types) win; mapping target fields fill in any
    field that has DLO data mapped but no relationship (kept as ``Unknown``).
    Sorting preserves the deterministic-output guarantee.
    """
    merged = dict(typed)
    for fd in mapping_fields:
        merged.setdefault(fd.name, fd)
    return tuple(sorted(merged.values(), key=lambda fd: fd.name.lower()))


def _fetch_dmo_details(
    base: str,
    api_version: str,
    dataspace: str,
    dmo_entries: list[tuple[str, str]],
    access_token: str,
    timeout: float,
    progress: ProgressFn | None = None,
) -> tuple[
    list[DataModelObject],
    list[Mapping],
    list[DmoFieldMapping],
    list[Relationship],
    list[str],
]:
    """Per-DMO: fetch mappings + relationships under ONE error boundary.

    A DMO whose mappings OR relationships call fails is logged and skipped — one
    bad DMO does not sink the whole document. Object-level mappings and field
    rows are de-duplicated across DMOs. Returns
    ``(dmos, mappings, dmo_field_mappings, relationships, skipped_names)``.
    """
    dmos: list[DataModelObject] = []
    mappings: list[Mapping] = []
    seen_maps: set[tuple[str, str]] = set()
    dmo_field_mappings: list[DmoFieldMapping] = []
    seen_field_rows: set[tuple[str, str, str, str]] = set()
    relationships: list[Relationship] = []
    seen_rels: set[tuple[str, str | None, str | None, str | None]] = set()
    skipped: list[str] = []
    total = len(dmo_entries)

    for done, (dmo_name, label) in enumerate(dmo_entries, start=1):
        if progress:
            progress(f"  DMOs {done}/{total}", True)
        try:
            dmo_maps, mapping_fields, field_rows = _fetch_dmo_mappings(
                base, api_version, dataspace, dmo_name, label, access_token, timeout
            )
            typed_fields, dmo_rels = _fetch_dmo_relationships(
                base, api_version, dataspace, dmo_name, access_token, timeout
            )
        except FetchError as exc:
            logger.warning("Skipping DMO %s: %s", dmo_name, exc)
            skipped.append(dmo_name)
            continue

        for m in dmo_maps:
            key = (m.source_dlo, m.target_dmo)
            if key not in seen_maps:
                seen_maps.add(key)
                mappings.append(m)
        for row in field_rows:
            row_key = (
                row.source_dlo_name,
                row.source_field_name,
                row.target_dmo_name,
                row.target_field_name,
            )
            if row_key not in seen_field_rows:
                seen_field_rows.add(row_key)
                dmo_field_mappings.append(row)
        for rel in dmo_rels:
            rel_key = (
                rel.source_dmo_name,
                rel.source_field,
                rel.related_entity,
                rel.related_field,
            )
            if rel_key not in seen_rels:
                seen_rels.add(rel_key)
                relationships.append(rel)
        dmos.append(
            DataModelObject(
                name=dmo_name,
                label=label,
                fields=_merge_dmo_fields(typed_fields, mapping_fields),
            )
        )
    if progress and total:
        progress("", False)  # end the in-place counter line
    return dmos, mappings, dmo_field_mappings, relationships, skipped


#: Candidate keys for a field mapping's human labels / source-field reference.
_SRC_FIELD_LABEL_KEYS: Final = ("sourceFieldLabel", "sourceLabel")
_TGT_FIELD_LABEL_KEYS: Final = ("targetFieldLabel", "targetLabel")
_DATA_SOURCE_FIELD_KEYS: Final = ("dataSourceField", "sourceFieldPath")


def _fetch_dmo_mappings(
    base: str,
    api_version: str,
    dataspace: str,
    dmo_name: str,
    dmo_label: str,
    access_token: str,
    timeout: float,
) -> tuple[list[Mapping], list[FieldDef], list[DmoFieldMapping]]:
    """Fetch one DMO's DLO→DMO mappings, target field names, and field rows.

    Returns ``(maps, target_fields, field_rows)``:

    - ``maps``: object-level DLO→DMO :class:`Mapping`s (de-duplicated here).
    - ``target_fields``: mapping-target field names (no type — the relationships
      endpoint supplies types; these come back ``Unknown`` and are merged later).
    - ``field_rows``: per-field :class:`DmoFieldMapping`s for Sheet 3. Field-level
      labels fall back to the API name (no Describe is available in Python, and
      Data Cloud ``__dll``/``__dlm`` objects are not describable anyway).
    """
    url = (
        f"{base}/services/data/{api_version}/ssot/data-model-object-mappings"
        f"?dataspace={dataspace}&dmoDeveloperName={dmo_name}"
    )
    body = get_json(url, access_token=access_token, timeout=timeout)
    maps: list[Mapping] = []
    seen: set[tuple[str, str]] = set()
    fields: dict[str, FieldDef] = {}
    field_rows: list[DmoFieldMapping] = []
    for entry in body.get("objectSourceTargetMaps", []):
        source_dlo = entry.get("sourceEntityDeveloperName")
        target_dmo = entry.get("targetEntityDeveloperName") or dmo_name
        if not source_dlo:
            continue
        source_dlo_label = entry.get("sourceEntityLabel") or source_dlo
        # The queried DMO's label applies when the target is the DMO we asked for.
        target_dmo_label = dmo_label if target_dmo == dmo_name else target_dmo

        key = (source_dlo, target_dmo)
        if key not in seen:
            seen.add(key)
            maps.append(Mapping(source_dlo=source_dlo, target_dmo=target_dmo))

        for fm in entry.get("fieldMappings", []):
            sf = fm.get("sourceFieldDeveloperName")
            tf = fm.get("targetFieldDeveloperName")
            if tf:
                fields.setdefault(tf, FieldDef(name=tf, type="Unknown"))
            if not sf or not tf:
                continue
            # Prefer real labels from the mapping payload; the DLO-field-label
            # join (in _enrich_dmo_field_mappings) fills any source label still
            # left as the API name. We never call Describe (it fails on __dlm).
            field_rows.append(
                DmoFieldMapping(
                    source_dlo_name=source_dlo,
                    source_dlo_label=source_dlo_label,
                    source_field_name=sf,
                    source_field_label=_first_str(fm, _SRC_FIELD_LABEL_KEYS) or sf,
                    target_dmo_name=target_dmo,
                    target_dmo_label=target_dmo_label,
                    target_field_name=tf,
                    target_field_label=_first_str(fm, _TGT_FIELD_LABEL_KEYS) or tf,
                    data_source_field=_first_str(fm, _DATA_SOURCE_FIELD_KEYS),
                )
            )
    return maps, list(fields.values()), field_rows


def _strip_custom_suffix(name: str) -> str:
    """Drop a single trailing ``__c``/``_c`` so DLO and mapping names join.

    DMO-mapping source fields carry a ``__c`` suffix the raw DLO field names do
    not (e.g. mapping ``Id__c`` ↔ DLO ``Id``; mapping ``SLASerialNumber__c`` ↔
    DLO ``SLASerialNumber_c``). Stripping one suffix from each side aligns them.
    """
    for suffix in ("__c", "_c"):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def _dlo_field_index(
    field_mappings: tuple[FieldMapping, ...],
) -> tuple[dict[tuple[str, str], str], dict[tuple[str, str], str]]:
    """Index DLO field labels and (reliable) types by ``(dlo, stripped name)``."""
    labels: dict[tuple[str, str], str] = {}
    types: dict[tuple[str, str], str] = {}
    for fm in field_mappings:
        if not fm.dlo_name or not fm.dlo_field_name:
            continue
        key = (fm.dlo_name, _strip_custom_suffix(fm.dlo_field_name))
        labels.setdefault(key, fm.dlo_field_label)
        types.setdefault(key, fm.data_type)
    return labels, types


def _enrich_dmo_field_mappings(
    rows: list[DmoFieldMapping],
    dlo_obj_label: dict[str, str],
    dlo_field_labels: dict[tuple[str, str], str],
) -> list[DmoFieldMapping]:
    """Fill DLO→DMO source labels from DLO metadata we already fetched.

    Only replaces a label that is still the API-name fallback (i.e. the mapping
    payload supplied no label of its own); real payload labels are left intact.
    Lookups are prebuilt by the caller (see :func:`_dlo_field_index`).
    """
    enriched: list[DmoFieldMapping] = []
    for r in rows:
        source_dlo_label = r.source_dlo_label
        if source_dlo_label == r.source_dlo_name:  # still the API-name fallback
            source_dlo_label = dlo_obj_label.get(r.source_dlo_name, source_dlo_label)

        source_field_label = r.source_field_label
        if source_field_label == r.source_field_name:  # still the API-name fallback
            label = dlo_field_labels.get(
                (r.source_dlo_name, _strip_custom_suffix(r.source_field_name))
            )
            if label:
                source_field_label = label

        enriched.append(
            replace(
                r,
                source_dlo_label=source_dlo_label,
                source_field_label=source_field_label,
            )
        )
    return enriched


def _enrich_dmo_field_types(
    dmos: list[DataModelObject],
    dmo_field_mappings: list[DmoFieldMapping],
    dlo_field_types: dict[tuple[str, str], str],
) -> list[DataModelObject]:
    """Replace generic/Unknown DMO field types with the mapped DLO field type.

    Acts only where a real DLO→DMO mapping exists and the DLO type is concrete.
    The resolved ``type`` token stays clean (e.g. ``Number``); the field's
    ``type_inferred`` flag records the provenance so renderers can mark it
    (e.g. "(via DLO)") without polluting the stored type. Unmapped/system DMO
    fields keep their original type. ``dlo_field_types`` is prebuilt by caller.
    """
    resolved: dict[tuple[str, str], str] = {}
    for r in dmo_field_mappings:
        dlo_type = dlo_field_types.get(
            (r.source_dlo_name, _strip_custom_suffix(r.source_field_name))
        )
        if dlo_type and dlo_type.lower() not in _GENERIC_DMO_TYPES:
            resolved.setdefault((r.target_dmo_name, r.target_field_name), dlo_type)

    if not resolved:
        return dmos

    out: list[DataModelObject] = []
    for dmo in dmos:
        changed = False
        new_fields: list[FieldDef] = []
        for fd in dmo.fields:
            if fd.type.lower() in _GENERIC_DMO_TYPES:
                dlo_type = resolved.get((dmo.name, fd.name))
                if dlo_type:
                    new_fields.append(replace(fd, type=dlo_type, type_inferred=True))
                    changed = True
                    continue
            new_fields.append(fd)
        out.append(replace(dmo, fields=tuple(new_fields)) if changed else dmo)
    return out
