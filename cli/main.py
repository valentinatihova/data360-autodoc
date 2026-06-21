"""``data360-autodoc`` command-line entry point.

Orchestrates the one-shot pipeline::

    auth (JWT bearer) -> fetch metadata -> render outputs -> write files

Outputs are selected with ``--format``:

- ``markdown`` — human-readable ``.md`` plus a ``.mmd`` Mermaid diagram
- ``json``     — deterministic ``.json`` snapshot (the drift-detection seam)
- ``pdf``      — not yet implemented (stub; warns and skips)
- ``all``      — markdown + json (+ pdf stub warning)

The ``.json`` snapshot is a first-class output, not a debug artifact: the paid
drift tier loads a prior snapshot and diffs it against a fresh fetch.
"""

from __future__ import annotations

import re
from pathlib import Path

import click

from fetcher.auth import (
    AUD_PRODUCTION,
    AUD_SANDBOX,
    DEFAULT_TOKEN_URL,
    SANDBOX_TOKEN_URL,
    AuthError,
    get_access_token,
)
from fetcher.metadata import MetadataError, fetch_metadata
from generator.markdown import render_markdown
from generator.mermaid import render_mermaid
from generator.snapshot import render_json

#: Valid values for the ``--format`` option.
FORMATS = ["markdown", "json", "pdf", "all"]


@click.group()
def cli() -> None:
    """Auto-generate documentation for Salesforce Data 360 orgs."""


@cli.command()
@click.option("--instance-url", required=True, help="Org base URL.")
@click.option("--client-id", required=True, help="Connected app consumer key.")
@click.option(
    "--private-key",
    "private_key_path",
    required=True,
    type=click.Path(exists=True, dir_okay=False),
    help="Path to the connected app's PEM private key.",
)
@click.option("--username", required=True, help="Salesforce username to impersonate.")
@click.option(
    "--output",
    "output_dir",
    default=".",
    type=click.Path(file_okay=False),
    help="Directory to write output files into (created if missing).",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(FORMATS),
    default="all",
    show_default=True,
    help="Which artifacts to generate.",
)
@click.option(
    "--sandbox",
    is_flag=True,
    default=False,
    help="Authenticate against test.salesforce.com (sandbox/scratch orgs).",
)
def generate(
    instance_url: str,
    client_id: str,
    private_key_path: str,
    username: str,
    output_dir: str,
    output_format: str,
    sandbox: bool,
) -> None:
    """Fetch an org's metadata and write documentation artifacts."""
    token_url = SANDBOX_TOKEN_URL if sandbox else DEFAULT_TOKEN_URL
    audience = AUD_SANDBOX if sandbox else AUD_PRODUCTION

    try:
        auth = get_access_token(
            instance_url=instance_url,
            client_id=client_id,
            private_key_path=private_key_path,
            username=username,
            token_url=token_url,
            audience=audience,
        )
        schema = fetch_metadata(
            instance_url=auth["instance_url"], access_token=auth["access_token"]
        )
    except (AuthError, MetadataError) as exc:
        # Surface a clean one-line error and exit non-zero — never a traceback.
        raise click.ClickException(str(exc)) from exc

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    base = _slug(schema.org_name) or "data360"

    written: list[str] = []
    want_markdown = output_format in ("markdown", "all")
    want_json = output_format in ("json", "all")
    want_pdf = output_format in ("pdf", "all")

    if want_markdown:
        md_path = out_dir / f"{base}.md"
        md_path.write_text(render_markdown(schema), encoding="utf-8")
        written.append(md_path.name)
        mmd_path = out_dir / f"{base}.mmd"
        mmd_path.write_text(render_mermaid(schema) + "\n", encoding="utf-8")
        written.append(mmd_path.name)

    if want_json:
        json_path = out_dir / f"{base}.json"
        json_path.write_text(render_json(schema), encoding="utf-8")
        written.append(json_path.name)

    if want_pdf:
        click.echo("PDF output is not yet implemented (stub) — skipping.", err=True)

    for name in written:
        click.echo(f"Wrote {name}")
    click.echo(
        f"Generated docs for {len(schema.dmos)} DMOs, "
        f"{len(schema.dlos)} DLOs, "
        f"{len(schema.identity_rulesets)} Identity Rulesets"
    )


def _slug(value: str) -> str:
    """Slugify an org name for use as an output filename stem."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


if __name__ == "__main__":  # pragma: no cover
    cli()
