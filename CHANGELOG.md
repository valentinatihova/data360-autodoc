# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project adheres to
semantic versioning.

## [Unreleased]

### Changed
- README opens with a short terminal demo GIF of `generate --target-org`
  (a real run, the wait sped up 30×).

## [0.4.1] - 2026-10-25

### Added
- `generate --strict`: fail and write nothing if any DMO could not be read,
  instead of a partial snapshot that `diff` would report as "DMO removed".
- README "Run drift checks in CI" recipe; the example GitHub Actions workflow
  now signs in with `sf org login jwt` + `--target-org`, uses a stable snapshot
  name (`--org-name`), `--strict`, and also runs on pull requests that change
  the baseline (skipped for forks, which get no secrets).
- `generate --diagram-image svg|png` draws the Mermaid diagram as an image
  next to the `.mmd` (for Confluence and other tools that don't render
  Mermaid). Uses mermaid-cli (`mmdc`) if installed; otherwise a warning with
  the install command, and the rest of the docs are written as usual.

### Changed
- `--format all` (the default) writes Markdown, Mermaid and JSON without the
  "PDF output is not yet implemented" line; PDF stays available only as
  `--format pdf` (still a stub).
- With `--target-org` and no `--org-name`, the document and its files are named
  after the alias (`my-org.md`) instead of the org's host name.
- README quick start mentions `pipx ensurepath` for first-time pipx users.

## [0.4.0] - 2026-10-22

### Added
- `generate --target-org ALIAS`: reuse an org you logged into with the
  Salesforce CLI (`sf org login web --alias ALIAS`); no connected app or JWT
  key needed. The token is taken from `sf org display` and never printed.
- Sign-in settings from the environment (`DATA360_TARGET_ORG`,
  `DATA360_ACCESS_TOKEN`, `DATA360_INSTANCE_URL`, `DATA360_CLIENT_ID`,
  `DATA360_PRIVATE_KEY`, `DATA360_USERNAME`), read only when no sign-in flag is
  given, so tokens stay out of the process list.
- `generate --org-name` (document title and file name) and `--verbose` (full
  error detail).
- A live "Listing DMOs… N scanned" counter while the DMO list loads.
- README opens with a screenshot and a full sample report generated from a
  Developer Edition org (`examples/sample-report/`, host redacted).
- `generate --all-dmos` documents every DMO. The default is enabled standard
  DMOs plus all custom DMOs (previously custom DMOs that were not enabled were
  dropped). The snapshot records the choice as `dmo_scope`, and `diff` warns
  (Markdown, JSON `warnings`, stderr) when two snapshots used different scopes.

### Changed
- Exactly one sign-in mode per run (`--target-org`, `--access-token`, or JWT);
  combining them is a usage error instead of one silently winning.
  `--instance-url` is no longer required with `--target-org`.
- Error messages are short and host-free (path, status and Salesforce
  `errorCode`), safe on a shared screen; `--verbose` shows the full URL and
  API response.
- README quick start leads with `pipx` / `uvx` and `--target-org`.

### Fixed
- An expired or invalid token (HTTP 401) no longer produces empty
  documentation: per-DMO 401s were skipped as "DMO errors", and version
  detection silently fell back to v62.0. The run now stops with a hint for the
  sign-in mode in use (e.g. `sf org login web --alias ALIAS`).
- `generate` failed on new orgs (for example a fresh Developer Edition with
  ~1,000 standard DMOs). The DMO list was requested as one 500-row page (about
  100 s, past the timeout). The endpoint returns no `nextPageUrl`, so DMOs past
  the first page were silently missed. The list is now read in 100-row pages by
  `offset`.
- DMOs with no relationships (HTTP 204) or no DLO mappings (HTTP 404) were
  skipped as errors after retries; they are now documented with empty sections.

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
