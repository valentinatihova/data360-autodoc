# TODO: Drift Detection (paid tier roadmap)

> **Status: deferred — do NOT build yet.** This is the paid-tier roadmap, locked
> by CEO review (2026-06-22). It builds on the deterministic `--format json`
> snapshot shipped in Phase 3 (`generator/snapshot.py`). The free CLI + README
> ship first (Phases 3–4); the drift engine is a later phase once those are live.

## Strategy context

- **Monetization:** free one-shot CLI (markdown + mermaid + json) vs paid
  recurring drift monitoring.
- **Access model:** **client-side drift, no credential custody.** The consultant
  runs the CLI on a schedule in their own environment with their own key and
  pushes JSON snapshots to the hosted service. We never hold client private keys.
  (Fully-hosted per-client OAuth Connected App is a possible v2.)
- **Open-core line:** the diff *engine* is free (in the CLI); the hosted
  *history + watching + reporting* is paid. The moat is "we remember and watch
  for you and produce the client report," not "we can subtract two JSON files."
- **ICP:** retainer / managed-service consultants and agencies — not one-and-done
  project consultants. Implies per-org or agency pricing, not a flat $49/seat
  (revisit when pricing).

## P1 — Free CLI: diff command

`data360-autodoc diff old.json new.json` → changeset.

- Input: two snapshot JSON files (the `--format json` output from `generate`).
- Load both via `generator.snapshot.load_json` (already round-trips losslessly).
- Compute a structured changeset over the two `OrgSchema`s:
  - DMOs/DLOs/CIOs/rulesets added, removed, renamed (label change)
  - per-object: fields added / removed / type-changed / key-qualifier-changed
  - mappings added / removed
- Output: human-readable summary (markdown) + machine-readable changeset (json).
- Deterministic and fully unit-tested with `responses`-free fixtures (pure data).
- Lives in the **free** CLI — adoption driver, hard to withhold.

## P2 — Runner template (for consultants)

A copy-paste scheduled-run pattern so consultants can automate snapshots in
*their* environment (no hosted credential custody).

- **cron example:** nightly `data360-autodoc generate --format json` into a
  dated snapshot dir, then `diff` against yesterday's snapshot.
- **GitHub Action example:** scheduled workflow that runs `generate`, commits the
  snapshot to a private repo (or uploads as an artifact), and optionally posts the
  changeset to Slack/email.
- Private key supplied via the runner's secret store (GH Actions secret / local
  env), never committed.
- Ship as `examples/` + a README section, not code we host.

## P3 — Hosted paid tier

The recurring-revenue layer a CLI structurally can't provide.

- **Snapshot history store:** consultant pushes snapshots; we retain the timeline
  per org.
- **Scheduled watching + alert delivery:** detect drift between the latest two
  snapshots and email the changelog.
- **Client-ready monthly changelog:** a shareable "what changed in your Data Cloud
  this month" report the consultant can forward or bill against.
- **Multi-org dashboard:** agency view across every org they're responsible for.

## Out of scope until post-revenue

- Impact / blast-radius graph ("change this DLO, what CIs break?")
- Fully-hosted per-client OAuth Connected App model (drift-tier v2)
- Client-facing hosted doc portals
