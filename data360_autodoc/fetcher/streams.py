"""Data Stream / Data Lake Object fetcher.

DLOs, Data Stream metadata, and field-mapping rows all come from a single
``/ssot/data-streams`` response. :func:`fetch_dlos_and_streams` returns all
three from **one** pass so the orchestrator hits the (slow) endpoint only once.

See ``agent_docs/api_reference.md`` for the verified response shape.
"""

from __future__ import annotations

from typing import Any

from data360_autodoc.fetcher._http import FetchError, iter_pages
from data360_autodoc.models import DataLakeObject, DataStream, FieldDef, FieldMapping

#: Connector-name lookup order, shared by stream + field-mapping rows.
_CONNECTOR_KEYS = ("connectorName", "name", "label", "displayName", "connectorType")


class StreamsError(RuntimeError):
    """Raised when Data Streams / DLOs cannot be retrieved."""


def fetch_dlos_and_streams(
    *, instance_url: str, access_token: str, api_version: str, timeout: float = 60.0
) -> tuple[
    tuple[DataLakeObject, ...], tuple[DataStream, ...], tuple[FieldMapping, ...]
]:
    """Fetch DLOs, Data Stream rows, and field-mapping rows in a single pass.

    Returns:
        ``(dlos, streams, field_mappings)`` — all from one pass over
        ``/ssot/data-streams``.

    Raises:
        StreamsError: If the data-streams request fails.
    """
    raw = _iter_raw_streams(
        instance_url=instance_url,
        access_token=access_token,
        api_version=api_version,
        timeout=timeout,
    )
    return (
        _build_dlos(raw),
        tuple(_parse_stream(s) for s in raw),
        _build_field_mappings(raw),
    )


def _iter_raw_streams(
    *, instance_url: str, access_token: str, api_version: str, timeout: float
) -> list[dict[str, Any]]:
    """Fetch every raw data-stream dict (paginated). Shared by both builders."""
    base = instance_url.rstrip("/")
    first_url = f"{base}/services/data/{api_version}/ssot/data-streams"
    raw: list[dict[str, Any]] = []
    try:
        for page in iter_pages(
            first_url, base_url=base, access_token=access_token, timeout=timeout
        ):
            for stream in page.get("dataStreams", []):
                if isinstance(stream, dict):
                    raw.append(stream)
    except FetchError as exc:
        raise StreamsError(str(exc)) from exc
    return raw


def _build_dlos(raw_streams: list[dict[str, Any]]) -> tuple[DataLakeObject, ...]:
    """Build de-duplicated DLOs from raw streams (first occurrence wins)."""
    by_name: dict[str, DataLakeObject] = {}
    for stream in raw_streams:
        dlo_info = stream.get("dataLakeObjectInfo")
        if not isinstance(dlo_info, dict):
            continue
        name = dlo_info.get("name")
        if not name or name in by_name:
            continue
        by_name[name] = _parse_dlo(dlo_info)
    return tuple(by_name.values())


def _parse_dlo(dlo_info: dict[str, Any]) -> DataLakeObject:
    """Build a DataLakeObject from a stream's ``dataLakeObjectInfo`` block."""
    name = dlo_info["name"]
    label = dlo_info.get("label") or name
    raw_fields = dlo_info.get("dataLakeFieldInfoRepresentation", []) or []
    fields = tuple(
        sorted(
            (_parse_field(f) for f in raw_fields),
            key=lambda fd: fd.name.lower(),
        )
    )
    return DataLakeObject(name=name, label=label, fields=fields)


def _parse_field(f: dict[str, Any]) -> FieldDef:
    """Build a FieldDef from a ``dataLakeFieldInfoRepresentation`` entry."""
    is_key = f.get("isPrimaryKey") is True
    return FieldDef(
        name=f["name"],
        type=f.get("dataType", "Unknown"),
        is_key=is_key,
        key_qualifier="PrimaryKey" if is_key else None,
    )


def _parse_stream(stream: dict[str, Any]) -> DataStream:
    """Build a DataStream row from one raw stream dict (mirrors the SI Apex)."""
    dlo_info = stream.get("dataLakeObjectInfo") or {}
    raw_fields = dlo_info.get("dataLakeFieldInfoRepresentation") or []

    pks: list[str] = []
    formula_fields: list[str] = []
    formula_calcs: list[str] = []
    for f in raw_fields:
        if not isinstance(f, dict):
            continue
        fname = f.get("name")
        if not fname:
            continue
        if f.get("isPrimaryKey") is True:
            pks.append(fname)
        if f.get("isFormula") is True or f.get("formula") is not None:
            formula_fields.append(fname)
            calc = f.get("formula") or f.get("calculation") or f.get("expression")
            formula_calcs.append("" if calc is None else str(calc))

    connector = stream.get("connectorInfo") or {}
    refresh = stream.get("refreshConfig") or {}
    adv = stream.get("advancedAttributes") or {}

    return DataStream(
        name=_first(stream, ("name", "label", "displayName", "developerName")) or "",
        dlo_name=dlo_info.get("name") or "",
        dlo_label=dlo_info.get("label") or dlo_info.get("name") or "",
        data_source=_first(connector, _CONNECTOR_KEYS),
        category=dlo_info.get("category"),
        event_time_field=dlo_info.get("eventDateTimeFieldName"),
        primary_keys=tuple(pks),
        formula_fields=tuple(formula_fields),
        formula_calculations=tuple(formula_calcs),
        org_unit_identifier=(
            dlo_info.get("organizationUnitIdentifier")
            or adv.get("organizationUnitIdentifier")
        ),
        schedule_frequency=_frequency(refresh),
        refresh_mode=refresh.get("refreshMode"),
        de_extraction_mode=_first(
            adv, ("dataExtensionExtractionMode", "extractionMode")
        ),
    )


def _build_field_mappings(
    raw_streams: list[dict[str, Any]],
) -> tuple[FieldMapping, ...]:
    """Build Sheet 2 rows: one per DLO field, with its source mapping.

    ``source_field`` is recovered from ``stream.sourceFields`` by matching the
    DLO field name to the source name with ``__`` collapsed to ``_`` (Data
    Cloud's field-naming rule, mirroring the SI Apex). System fields (``KQ_``,
    ``cdp_sys_``, …) have no source and stay blank. ``is_foreign_key`` is the
    ``KQ_``-prefix heuristic.
    """
    rows: list[FieldMapping] = []
    for stream in raw_streams:
        dlo_info = stream.get("dataLakeObjectInfo")
        if not isinstance(dlo_info, dict):
            continue
        stream_name = (
            _first(stream, ("name", "label", "displayName", "developerName")) or ""
        )
        data_source = _first(stream.get("connectorInfo") or {}, _CONNECTOR_KEYS)

        # source name keyed by its DLO-normalized form (`__` -> `_`).
        source_by_dlo_name: dict[str, str] = {}
        for sf in stream.get("sourceFields") or []:
            if isinstance(sf, dict):
                src = sf.get("name")
                if src:
                    source_by_dlo_name[src.replace("__", "_")] = src

        dlo_name = dlo_info.get("name") or ""
        for f in dlo_info.get("dataLakeFieldInfoRepresentation") or []:
            if not isinstance(f, dict):
                continue
            fname = f.get("name")
            if not fname:
                continue
            rows.append(
                FieldMapping(
                    stream_name=stream_name,
                    source_field=source_by_dlo_name.get(fname),
                    dlo_field_label=f.get("label") or fname,
                    dlo_field_name=fname,
                    data_type=f.get("dataType", "Unknown"),
                    is_primary_key=f.get("isPrimaryKey") is True,
                    is_foreign_key=fname.startswith("KQ_"),
                    data_source=data_source,
                    dlo_name=dlo_name,
                    nullable=_nullable(f),
                )
            )
    return tuple(rows)


def _nullable(f: dict[str, Any]) -> bool | None:
    """Read nullability from a field rep if the source exposes it, else None.

    ``/ssot/data-streams`` for file/CRM streams in the verified org does not
    return a nullability attribute, so this is ``None`` (rendered blank). We
    still read the known key spellings so that any org which *does* expose it
    populates the column without code changes — we never assume a default.
    """
    for key in ("nullable", "isNullable", "nillable"):
        v = f.get(key)
        if isinstance(v, bool):
            return v
    return None


def _first(d: dict[str, Any], keys: tuple[str, ...]) -> str | None:
    """Return the first non-empty value among ``keys`` as a string, else None."""
    for k in keys:
        v = d.get(k)
        if v not in (None, ""):
            return str(v)
    return None


def _frequency(refresh: dict[str, Any]) -> str | None:
    """Extract a schedule frequency from ``refreshConfig.frequency``."""
    freq = refresh.get("frequency")
    if isinstance(freq, dict):
        ftype = freq.get("frequencyType")
        return str(ftype) if ftype is not None else None
    return str(freq) if freq is not None else None
