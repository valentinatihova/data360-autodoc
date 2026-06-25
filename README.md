# data360-autodoc

[![PyPI version](https://img.shields.io/badge/pypi-coming%20soon-blue)](https://pypi.org/project/data360-autodoc/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Auto-generate human-readable documentation for Salesforce Data 360 (Data Cloud) orgs — in seconds, not days.**

Point it at an org and it produces a full data dictionary (DMOs, DLOs, fields, keys), an ERD of your DLO → DMO mappings, and a deterministic JSON snapshot.

- 📓 **Data dictionary** — every DMO and DLO as clean Markdown tables, with field names, types, and keys.
- 🔗 **ERD diagram** — a Mermaid `graph LR` of how your Data Lake Objects map into Data Model Objects.
- 🧊 **JSON snapshot** — a deterministic, diff-friendly export of your whole org schema (the foundation for drift detection — see below).

## For who

Built for **Salesforce SI consultants and Data Cloud practitioners** who lose days hand-writing org documentation for every engagement. Works against any Data 360 org you can authenticate to with a connected app — including **Developer Edition / Data Cloud Dev orgs**, so you can try it on a sandbox before pointing it at a client.

## Quick start

```bash
pip install data360-autodoc

data360-autodoc generate \
  --instance-url https://mydomain.my.salesforce.com \
  --client-id <connected-app-consumer-key> \
  --private-key ./server.pem \
  --username admin@myorg.com \
  --output ./docs \
  --format all
```

```
Wrote acme-data-cloud.md
Wrote acme-data-cloud.mmd
Wrote acme-data-cloud.json
Generated docs for 24 DMOs, 11 DLOs, 0 Identity Rulesets
```

Authentication uses the **OAuth 2.0 JWT Bearer flow** (connected app + private key — no passwords stored).

**Options that affect the metadata fetch:**

- `--sandbox` — authenticate against `test.salesforce.com` (sandbox / scratch orgs).
- `--api-version` — the Salesforce REST API version used for the `/ssot/*` metadata calls (e.g. `v62.0`). **By default the tool auto-detects your org's highest supported version** (from `GET /services/data/`), so you normally don't set this. Force it only if auto-detection picks a version where a Data Cloud endpoint misbehaves, or to pin output to a specific version. It must be a valid Salesforce REST API version your org supports.

(The `Identity Rulesets` count is currently always `0` — see "Not supported yet" below.)

## What you get

`--format` controls the output:

| Format | Files | What it is |
|--------|-------|------------|
| `markdown` | `.md` + `.mmd` | Data dictionary + Mermaid ERD |
| `json` | `.json` | Deterministic org-schema snapshot |
| `pdf` | — | _Coming soon_ |
| `all` | all of the above | Everything |

### Example output

The Markdown data dictionary (DMO field types come from the org's relationships metadata; DLO keys from the data streams):

```markdown
## Data Model Objects (DMOs)

### Individual (`Individual__dmo`)

| Name | Type | Key |
| --- | --- | --- |
| Email__c | EmailAddress |  |
| Id__c | Text |  |

## Data Lake Objects (DLOs)

### Order (Home) (`Order_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| Amount | Number |  |
| OrderId | Text | PrimaryKey |
```

The ERD (renders natively in GitHub):

```mermaid
graph LR
  Order_Home__dll["Order (Home)"]
  Individual__dmo["Individual"]
  Order_Home__dll --> Individual__dmo
```

Output is **deterministic** — the same org always produces byte-identical docs (collections are sorted alphabetically). That makes the output safe to commit and easy to diff.

### What it reads — and what it doesn't yet

Under the hood it calls the **Data 360 Connect REST API** (`/services/data/v…/ssot/*`): `data-model-objects` (DMOs), `data-model-object-mappings` (DLO→DMO mappings + field names), `…/{dmo}/relationships` (real DMO field types), and `data-streams` (DLOs + their fields, including primary keys). Full request/response shapes are in [`agent_docs/api_reference.md`](agent_docs/api_reference.md).

**Not supported yet.** Calculated Insights and Identity Resolution rulesets are **not fetched** — those sections render as empty placeholders (e.g. `_No Calculated Insights found._`) and the `Identity Rulesets` count stays `0`. Documenting them is on the roadmap. (Profile and Engagement DMOs *are* covered — those are DMO categories, not separate entities.)

**Resilient by default.** If one DMO's metadata can't be read, that DMO is skipped with a warning and the rest of the document is still produced. If the org has more than 500 DMOs, the list is capped (with a warning). A failure fetching the DMO list or the data streams stops the run with a clean one-line error — never a stack trace.

## Future: drift monitoring (paid tier)

The open-source CLI documents your org once. The thing that actually bites consultants is when an org **changes** after you've documented it — a client admin adds a DLO, a field type changes, an identity rule shifts — and your beautiful docs quietly go stale.

A hosted tier (planned) will turn the deterministic JSON snapshot into **drift monitoring**: re-run on a schedule, diff today's snapshot against the last one, and get a client-ready changelog of exactly what changed — without ever handing over your org credentials (drift runs in your own environment; the hosted service only stores snapshots and sends alerts). The CLI stays free forever; the recurring watching, history, and multi-org dashboard are the paid layer.

## Hosted version

A hosted web UI is in the works at **[data360doc.com](https://data360doc.com)** _(placeholder)_ — same docs, plus scheduled drift alerts and a multi-org dashboard for agencies.

## License

MIT
