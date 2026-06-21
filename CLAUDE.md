Project
CLI + SaaS tool that auto-generates human-readable documentation for Salesforce Data 360 orgs.
Target: Salesforce SI consultants, Data Cloud practitioners.
Stack: Python 3.11+, FastAPI, WeasyPrint, Mermaid.js, AWS S3.
Repo: data360-autodoc (MIT license, open-core model)

Architecture
text
data360doc/
├── cli/              # CLI entry point (data360-autodoc command)
├── fetcher/          # Salesforce Data 360 API clients
│   ├── metadata.py   # GET /api/v1/metadata/ — DMOs, DLOs, CIOs
│   ├── identity.py   # Identity Resolution rules
│   └── streams.py    # Data Streams + DLO schema
├── generator/        # Document generators
│   ├── markdown.py   # Markdown output
│   ├── pdf.py        # PDF via WeasyPrint
│   └── mermaid.py    # ERD diagram (Mermaid syntax)
├── api/              # FastAPI web app (hosted SaaS version)
├── tests/            # pytest unit + integration tests
└── agent_docs/       # Extended docs referenced from this file
    ├── api_reference.md
    ├── auth_flow.md
    └── output_format_spec.md
Conventions
Python: black formatter, type hints everywhere, docstrings on all public functions

API calls: always use exponential backoff (max 3 retries) for Salesforce API

Auth: OAuth 2.0 JWT Bearer Flow only — NEVER store credentials in code

Output: deterministic — same org input → same Markdown output (sorted alphabetically)

Tests: every fetcher function must have a mock test using responses library

Never hardcode: org URLs, client_id, client_secret, instance URLs

Definition of Done
A task is done when:

Code passes pytest with no failures

black . reports no changes

CLI runs end-to-end against a Developer Edition org (or mock)

Markdown output renders correctly in GitHub preview

No secrets in any committed file

Key APIs (see agent_docs/api_reference.md for full reference)
Data 360 Metadata: GET {instance_url}/api/v1/metadata/

DLO Schema: GET {instance_url}/services/data/v62.0/ssot/metadata/dlo/{name}

Identity Resolution: Metadata API via SFDX CLI

Auth token: POST {instance_url}/services/oauth2/token (JWT flow)

Never Touch
generator/pdf.py font settings (WeasyPrint quirks, tested)

.github/workflows/release.yml without explicit approval