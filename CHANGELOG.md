# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project adheres to
semantic versioning.

## [Unreleased]

### Fixed
- `generate` failed on new orgs (for example a fresh Developer Edition with
  ~1,000 standard DMOs). The DMO list was requested as one 500-row page (about
  100 s, past the timeout). The endpoint returns no `nextPageUrl`, so DMOs past
  the first page were silently missed. The list is now read in 100-row pages by
  `offset`.
- DMOs with no relationships (HTTP 204) or no DLO mappings (HTTP 404) were
  skipped as errors after retries; they are now documented with empty sections.

### Added
- `generate --all-dmos` documents every DMO. The default is enabled standard
  DMOs plus all custom DMOs (previously custom DMOs that were not enabled were
  dropped). The snapshot records the choice as `dmo_scope`, and `diff` warns
  (Markdown, JSON `warnings`, stderr) when two snapshots used different scopes.

## [0.3.0] - 2026-10-21

### Added
- **Schema drift detection**: `data360-autodoc diff OLD.json NEW.json` compares
  two JSON snapshots and reports added / removed / changed DMOs and DLOs, their
  fields (`type`, `is_key`, `key_qualifier`), data streams and their
  Stream → DLO field mappings, DLO → DMO object and field mappings, and DMO
  relationships (`cardinality`, `status`, label). No org
  credentials needed — it only reads the snapshot files.
- `diff --format markdown|json`: a human-readable Markdown report (fits a PR
  comment or a GitHub Actions job summary) or a machine-readable JSON report
  with `has_changes`, `change_count` and a per-area summary.
- `diff --fail-on-change` exits `1` when drift is found, for CI gates; an
  unreadable, malformed or incompatible snapshot (or an unwritable report)
  exits `2`, so an error is never mistaken for drift. `--output FILE` writes the
  report to a file.
- Example GitHub Actions workflow
  (`examples/github-actions/data360-drift.yml`) that snapshots an org on a
  schedule and fails on drift against a committed baseline.
- Synthetic before/after snapshot fixtures (`tests/fixtures/acme-*.json`).

### Changed
- Releases are published to PyPI from GitHub Actions (Trusted Publishing) when
  a GitHub Release is created.
- Tests and `black --check` now run in GitHub Actions on Python 3.11–3.14 for
  every pull request and push to `main`; the README badge shows the live status.

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
