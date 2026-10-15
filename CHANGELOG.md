# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project adheres to
semantic versioning.

## [Unreleased]

### Added
- **Schema drift detection**: `data360-autodoc diff OLD.json NEW.json` compares
  two JSON snapshots and reports added / removed / changed DMOs and DLOs, their
  fields (`type`, `is_key`, `key_qualifier`), DLO → DMO object and field
  mappings, and DMO relationships (`cardinality`, `status`, label). No org
  credentials needed — it only reads the snapshot files.
- `diff --format markdown|json`: a human-readable Markdown report (fits a PR
  comment or a GitHub Actions job summary) or a machine-readable JSON report
  with `has_changes`, `change_count` and a per-area summary.
- `diff --fail-on-change` exits `1` when drift is found, for CI gates; an
  unreadable or incompatible snapshot exits `2`. `--output FILE` writes the
  report to a file.
- Example GitHub Actions workflow
  (`examples/github-actions/data360-drift.yml`) that snapshots an org on a
  schedule and fails on drift against a committed baseline.
- Synthetic before/after snapshot fixtures (`tests/fixtures/acme-*.json`).

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
