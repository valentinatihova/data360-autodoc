"""``data360-autodoc`` command-line entry point.

Orchestrates the one-shot pipeline::

    auth (JWT bearer) -> fetch metadata -> render outputs -> write files

Outputs are selected with ``--format``:

- ``markdown`` — human-readable ``.md`` plus a ``.mmd`` Mermaid diagram
- ``json``     — deterministic ``.json`` snapshot (the drift-detection seam)
- ``pdf``      — not yet implemented (stub; warns and skips)
- ``all``      — markdown + json (+ pdf stub warning)

The ``.json`` snapshot is a first-class output, not a debug artifact: the
``diff`` command loads two snapshots and reports the schema drift between them::

    data360-autodoc diff old.json new.json [--format markdown|json]
        [--output FILE] [--fail-on-change]

``diff`` exit codes: ``0`` no drift (or drift without ``--fail-on-change``),
``1`` drift detected with ``--fail-on-change``, ``2`` any error (unreadable or
malformed snapshot, unwritable report, usage error).
"""

from __future__ import annotations

import re
from pathlib import Path

import click

from data360_autodoc.diff import diff_schemas
from data360_autodoc.fetcher.auth import (
    AUD_PRODUCTION,
    AUD_SANDBOX,
    DEFAULT_TOKEN_URL,
    SANDBOX_TOKEN_URL,
    AuthError,
    get_access_token,
)
from data360_autodoc.fetcher.metadata import MetadataError, fetch_metadata
from data360_autodoc.generator.drift import render_diff_json, render_diff_markdown
from data360_autodoc.generator.markdown import render_markdown
from data360_autodoc.generator.mermaid import render_mermaid
from data360_autodoc.generator.snapshot import load_json, render_json
from data360_autodoc.models import OrgSchema

#: Valid values for the ``--format`` option.
FORMATS = ["markdown", "json", "pdf", "all"]

#: Valid values for ``diff --format``.
DIFF_FORMATS = ["markdown", "json"]

#: ``diff --fail-on-change`` exit status when drift is found (like ``diff(1)``).
EXIT_DRIFT = 1

#: ``diff`` exit status for an unreadable snapshot (kept distinct from drift).
EXIT_ERROR = 2


@click.group()
def cli() -> None:
    """Auto-generate documentation for Salesforce Data 360 orgs."""


@cli.command()
@click.option("--instance-url", required=True, help="Org base URL.")
@click.option(
    "--access-token",
    default=None,
    help="Use a pre-obtained OAuth access token and skip JWT auth. When set, "
    "--client-id / --private-key / --username are not needed.",
)
@click.option(
    "--client-id", default=None, help="Connected app consumer key (JWT auth)."
)
@click.option(
    "--private-key",
    "private_key_path",
    default=None,
    type=click.Path(exists=True, dir_okay=False),
    help="Path to the connected app's PEM private key (JWT auth).",
)
@click.option(
    "--username", default=None, help="Salesforce username to impersonate (JWT auth)."
)
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
@click.option(
    "--api-version",
    "api_version",
    default=None,
    help="Data API version (e.g. v62.0). Default: auto-detect the org's highest.",
)
@click.option(
    "--timeout",
    default=120.0,
    show_default=True,
    type=float,
    help="Per-request timeout (seconds) for metadata calls. Data Cloud is slow.",
)
def generate(
    instance_url: str,
    access_token: str | None,
    client_id: str | None,
    private_key_path: str | None,
    username: str | None,
    output_dir: str,
    output_format: str,
    sandbox: bool,
    api_version: str | None,
    timeout: float,
) -> None:
    """Fetch an org's metadata and write documentation artifacts."""
    if access_token:
        token = access_token
        org_url = instance_url
    else:
        missing = [
            flag
            for flag, value in (
                ("--client-id", client_id),
                ("--private-key", private_key_path),
                ("--username", username),
            )
            if not value
        ]
        if missing:
            raise click.UsageError(
                "Provide --access-token, or all of --client-id, --private-key, "
                f"--username for JWT auth. Missing: {', '.join(missing)}."
            )
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
        except AuthError as exc:
            raise click.ClickException(str(exc)) from exc
        token = auth["access_token"]
        org_url = auth["instance_url"]

    def _progress(message: str, inline: bool) -> None:
        # Progress goes to stderr so it never pollutes the doc output. inline
        # uses a carriage return to update the DMO counter in place.
        if inline:
            click.echo(f"\r{message}", nl=False, err=True)
        else:
            click.echo(message, err=True)

    try:
        schema = fetch_metadata(
            instance_url=org_url,
            access_token=token,
            api_version=api_version,
            timeout=timeout,
            progress=_progress,
        )
    except MetadataError as exc:
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


@cli.command()
@click.argument("old_snapshot", type=click.Path(exists=True, dir_okay=False))
@click.argument("new_snapshot", type=click.Path(exists=True, dir_okay=False))
@click.option(
    "--format",
    "output_format",
    type=click.Choice(DIFF_FORMATS),
    default="markdown",
    show_default=True,
    help="Report format: human-readable Markdown or machine-readable JSON.",
)
@click.option(
    "--output",
    "output_path",
    default=None,
    type=click.Path(dir_okay=False),
    help="Write the report to this file instead of stdout.",
)
@click.option(
    "--fail-on-change",
    is_flag=True,
    default=False,
    help=f"Exit with status {EXIT_DRIFT} when any drift is detected (for CI).",
)
def diff(
    old_snapshot: str,
    new_snapshot: str,
    output_format: str,
    output_path: str | None,
    fail_on_change: bool,
) -> None:
    """Compare two JSON snapshots and report schema drift.

    OLD_SNAPSHOT and NEW_SNAPSHOT are .json files written by
    `generate --format json`. Reports added, removed and changed DMOs, DLOs,
    fields, data streams, Stream -> DLO and DLO -> DMO mappings and DMO
    relationships.
    """
    old, new = _load_snapshot(old_snapshot), _load_snapshot(new_snapshot)
    render = render_diff_json if output_format == "json" else render_diff_markdown
    try:
        result = diff_schemas(old, new)
        report = render(result)
    except (AttributeError, TypeError) as exc:
        # Valid JSON with wrongly typed values (e.g. a null name).
        raise _diff_error(f"Malformed snapshot data: {exc}") from exc

    if output_path:
        out = Path(output_path)
        try:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(report, encoding="utf-8")
        except OSError as exc:
            raise _diff_error(f"Could not write report {output_path}: {exc}")
        click.echo(f"Wrote {out.name}")
    else:
        click.echo(report, nl=False)

    # Summary goes to stderr so stdout stays a clean report when piped.
    if result.has_changes:
        n = result.change_count
        click.echo(f"Schema drift: {n} change{'s' if n != 1 else ''}", err=True)
    else:
        click.echo("No schema drift.", err=True)

    if fail_on_change and result.has_changes:
        raise SystemExit(EXIT_DRIFT)


def _load_snapshot(path: str) -> OrgSchema:
    """Load a snapshot file, turning any parse problem into a clean CLI error."""
    try:
        return load_json(Path(path).read_text(encoding="utf-8"))
    except KeyError as exc:
        message = f"missing required key {exc}"
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        message = str(exc)
    raise _diff_error(f"Could not read snapshot {path}: {message}")


def _diff_error(message: str) -> click.ClickException:
    """A ``diff`` failure that exits ``EXIT_ERROR`` — never mistaken for drift."""
    error = click.ClickException(message)
    error.exit_code = EXIT_ERROR
    return error


def _slug(value: str) -> str:
    """Slugify an org name for use as an output filename stem."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


if __name__ == "__main__":  # pragma: no cover
    cli()
