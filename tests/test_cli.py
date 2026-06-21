"""Tests for the Click CLI (auth + fetch are mocked — no network)."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest
from click.testing import CliRunner

from cli import main as cli_main
from models import (
    DataLakeObject,
    DataModelObject,
    IdentityResolutionRuleset,
    Mapping,
    OrgSchema,
)

FIXED_TS = datetime(2026, 6, 21, 17, 30, 0, tzinfo=timezone.utc)


def _fixture_schema() -> OrgSchema:
    return OrgSchema(
        org_name="Acme Data Cloud",
        instance_url="https://acme.my.salesforce.com",
        generated_at=FIXED_TS,
        dmos=(DataModelObject(name="Individual__dmo", label="Individual"),),
        dlos=(DataLakeObject(name="Order_Home__dll", label="Order"),),
        identity_rulesets=(
            IdentityResolutionRuleset(name="Default_Ruleset", label="Default"),
        ),
        mappings=(Mapping(source_dlo="Order_Home__dll", target_dmo="Individual__dmo"),),
    )


@pytest.fixture(autouse=True)
def _mock_pipeline(monkeypatch: pytest.MonkeyPatch) -> None:
    """Stub auth + metadata fetch so the CLI runs offline."""
    monkeypatch.setattr(
        cli_main,
        "get_access_token",
        lambda **kwargs: {
            "access_token": "TOK",
            "instance_url": kwargs["instance_url"],
        },
    )
    monkeypatch.setattr(cli_main, "fetch_metadata", lambda **kwargs: _fixture_schema())


@pytest.fixture
def key_file(tmp_path: Path) -> str:
    f = tmp_path / "server.pem"
    f.write_text("dummy-key", encoding="utf-8")
    return str(f)


def _args(key: str, out: Path, fmt: str) -> list[str]:
    return [
        "generate",
        "--instance-url",
        "https://acme.my.salesforce.com",
        "--client-id",
        "3MVG9abc",
        "--private-key",
        key,
        "--username",
        "admin@acme.com",
        "--output",
        str(out),
        "--format",
        fmt,
    ]


def test_format_all_writes_md_mmd_json(key_file: str, tmp_path: Path) -> None:
    out = tmp_path / "docs"
    result = CliRunner().invoke(cli_main.cli, _args(key_file, out, "all"))
    assert result.exit_code == 0, result.output
    assert (out / "acme-data-cloud.md").exists()
    assert (out / "acme-data-cloud.mmd").exists()
    assert (out / "acme-data-cloud.json").exists()


def test_summary_line(key_file: str, tmp_path: Path) -> None:
    result = CliRunner().invoke(cli_main.cli, _args(key_file, tmp_path, "all"))
    assert "Generated docs for 1 DMOs, 1 DLOs, 1 Identity Rulesets" in result.output


def test_format_json_only(key_file: str, tmp_path: Path) -> None:
    out = tmp_path / "json-only"
    result = CliRunner().invoke(cli_main.cli, _args(key_file, out, "json"))
    assert result.exit_code == 0, result.output
    assert (out / "acme-data-cloud.json").exists()
    assert not (out / "acme-data-cloud.md").exists()
    assert not (out / "acme-data-cloud.mmd").exists()


def test_format_markdown_no_json(key_file: str, tmp_path: Path) -> None:
    out = tmp_path / "md-only"
    result = CliRunner().invoke(cli_main.cli, _args(key_file, out, "markdown"))
    assert result.exit_code == 0, result.output
    assert (out / "acme-data-cloud.md").exists()
    assert not (out / "acme-data-cloud.json").exists()


def test_pdf_is_stubbed(key_file: str, tmp_path: Path) -> None:
    result = CliRunner().invoke(cli_main.cli, _args(key_file, tmp_path, "pdf"))
    assert result.exit_code == 0, result.output
    assert "not yet implemented" in result.output
    assert not list(tmp_path.glob("*.pdf"))


def test_output_dir_created(key_file: str, tmp_path: Path) -> None:
    out = tmp_path / "nested" / "deep"
    result = CliRunner().invoke(cli_main.cli, _args(key_file, out, "json"))
    assert result.exit_code == 0, result.output
    assert out.is_dir()


def test_missing_required_option_errors(key_file: str, tmp_path: Path) -> None:
    result = CliRunner().invoke(
        cli_main.cli,
        ["generate", "--client-id", "x", "--private-key", key_file],
    )
    assert result.exit_code != 0
    assert "instance-url" in result.output


def test_auth_failure_is_clean_not_traceback(
    key_file: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from fetcher.auth import AuthError

    def _boom(**kwargs):
        raise AuthError("JWT bearer exchange rejected (400): invalid_grant")

    monkeypatch.setattr(cli_main, "get_access_token", _boom)
    result = CliRunner().invoke(cli_main.cli, _args(key_file, tmp_path, "all"))
    assert result.exit_code != 0
    # Clean Click error, no raw traceback leaking the exception class.
    assert "invalid_grant" in result.output
    assert "Traceback" not in result.output


def test_snapshot_round_trips_from_written_file(key_file: str, tmp_path: Path) -> None:
    out = tmp_path / "rt"
    CliRunner().invoke(cli_main.cli, _args(key_file, out, "json"))
    from generator.snapshot import load_json

    schema = load_json((out / "acme-data-cloud.json").read_text(encoding="utf-8"))
    assert schema.org_name == "Acme Data Cloud"
    assert [d.name for d in schema.dmos] == ["Individual__dmo"]
