# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project adheres to
semantic versioning.

## [0.2.0] - 2026-06-26

### Added
- **Data Streams section** (Sheet 1): per-stream source/refresh metadata
  (DataSource, Category, EventTimeField, PrimaryKey, ScheduleFrequency,
  RefreshMode, …) from `/ssot/data-streams`.
- **Field Mapping (Streams → DLO) section** (Sheet 2): one row per Data Lake
  field with source/DLO labels, data type, primary key, DLO API name, and a
  `KQ_`-prefix foreign-key heuristic. Single-pass fetch shares the streams call.
- **DLO → DMO Field Mappings section** (Sheet 3): field-level source→target
  mappings grouped by source/target pairing, with real labels joined from DLO
  field metadata (no Describe needed).
- **Relationships section**: DMO-to-DMO relationships parsed from the verified
  `sourceObject`/`targetObject` payload of
  `/ssot/data-model-objects/{dmo}/relationships`, with normalized cardinality
  (`ManyToOne` → `N:1`) and a `Status` column so inactive standard
  relationships stay visible. Previously this payload was fetched and discarded.
- **Mermaid relationship edges**: active DMO→DMO relationships render as dashed,
  cardinality-labeled edges alongside the solid DLO→DMO mapping edges.
- DMO field types are now resolved from the mapped DLO field type when the DMO
  endpoint returns a generic/`Unknown` type, marked `(via DLO)` in the document
  and tracked by an explicit `type_inferred` flag (the stored type stays clean).
- JSON snapshot serializes all new metadata (streams, field mappings, DMO field
  mappings, relationships) and round-trips losslessly.

### Changed
- `Nullable` in the Streams → DLO section is shown only when the source exposes
  it; `/ssot/data-streams` does not, so it stays blank (never guessed).
- `agent_docs/api_reference.md` updated to the verified relationships payload
  shape.

### Removed
- Redundant `fetch_dlos` / `fetch_data_streams` wrappers (the orchestrator uses
  the single-pass `fetch_dlos_and_streams`); their test coverage was preserved.
