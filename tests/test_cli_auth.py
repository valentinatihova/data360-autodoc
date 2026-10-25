"""Tests for generate's auth selection, env fallback, 401 hints and options."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest
from click.testing import CliRunner

from data360_autodoc.cli import main as cli_main
from data360_autodoc.fetcher.metadata import MetadataError, MetadataUnauthorized
from data360_autodoc.fetcher.sf_cli import SfCliError
from data360_autodoc.models import OrgSchema

URL = "https://acme.my.salesforce.com"


def _runner() -> CliRunner:
    """Keep stderr apart from stdout on every supported Click (8.1 needs a flag)."""
    try:
        return CliRunner(mix_stderr=False)
    except TypeError:
        return CliRunner()


@pytest.fixture(autouse=True)
def _offline(monkeypatch: pytest.MonkeyPatch) -> dict:
    """Stub every auth backend and the fetch; record what fetch received."""
    for name in cli_main.AUTH_ENV.values():
        monkeypatch.delenv(name, raising=False)
    monkeypatch.delenv("DATA360_INSTANCE_URL", raising=False)
    seen: dict = {}

    def fake_sf(alias: str) -> tuple[str, str]:
        seen["alias"] = alias
        return URL, "SF-TOKEN"

    monkeypatch.setattr(cli_main, "org_credentials", fake_sf)
    monkeypatch.setattr(
        cli_main,
        "get_access_token",
        lambda **kw: {"access_token": "JWT-TOKEN", "instance_url": kw["instance_url"]},
    )

    def fake_fetch(**kwargs):
        seen.update(kwargs)
        return OrgSchema(
            org_name=kwargs.get("org_name") or "acme.my.salesforce.com",
            instance_url=kwargs["instance_url"],
            generated_at=datetime(2026, 10, 22, tzinfo=timezone.utc),
        )

    monkeypatch.setattr(cli_main, "fetch_metadata", fake_fetch)
    return seen


def _generate(tmp_path: Path, *args: str, env: dict | None = None):
    return _runner().invoke(
        cli_main.cli,
        ["generate", "--output", str(tmp_path), "--format", "json", *args],
        env=env,
    )


@pytest.fixture
def key_file(tmp_path: Path) -> str:
    f = tmp_path / "server.pem"
    f.write_text("dummy-key", encoding="utf-8")
    return str(f)


# --------------------------------------------------------------------------- #
# One auth mode
# --------------------------------------------------------------------------- #


def test_target_org_needs_no_instance_url(tmp_path: Path, _offline: dict) -> None:
    result = _generate(tmp_path, "--target-org", "acme")
    assert result.exit_code == 0, result.output
    assert _offline["alias"] == "acme"
    assert _offline["access_token"] == "SF-TOKEN"
    assert _offline["instance_url"] == URL


def test_access_token_mode(tmp_path: Path, _offline: dict) -> None:
    result = _generate(tmp_path, "--instance-url", URL, "--access-token", "T")
    assert result.exit_code == 0, result.output
    assert _offline["access_token"] == "T"


def test_jwt_mode(tmp_path: Path, key_file: str, _offline: dict) -> None:
    result = _generate(
        tmp_path,
        "--instance-url",
        URL,
        "--client-id",
        "C",
        "--private-key",
        key_file,
        "--username",
        "u@acme.com",
    )
    assert result.exit_code == 0, result.output
    assert _offline["access_token"] == "JWT-TOKEN"


def test_no_credentials_lists_the_options(tmp_path: Path) -> None:
    result = _generate(tmp_path, "--instance-url", URL)
    assert result.exit_code == 2
    assert "--target-org" in result.output + result.stderr
    assert "--access-token" in result.output + result.stderr


@pytest.mark.parametrize(
    "args",
    [
        ("--target-org", "acme", "--access-token", "T"),
        ("--access-token", "T", "--client-id", "C"),
        ("--target-org", "acme", "--username", "u@acme.com"),
    ],
)
def test_two_auth_modes_are_rejected(tmp_path: Path, args: tuple) -> None:
    result = _generate(tmp_path, "--instance-url", URL, *args)
    assert result.exit_code == 2
    assert "exactly one way to sign in" in result.output + result.stderr


def test_partial_jwt_names_what_is_missing(tmp_path: Path) -> None:
    result = _generate(tmp_path, "--instance-url", URL, "--client-id", "C")
    assert result.exit_code == 2
    assert "Missing: --private-key, --username" in result.output + result.stderr


def test_missing_private_key_file(tmp_path: Path) -> None:
    result = _generate(
        tmp_path,
        "--instance-url",
        URL,
        "--client-id",
        "C",
        "--private-key",
        str(tmp_path / "nope.pem"),
        "--username",
        "u",
    )
    assert result.exit_code == 2
    assert "Private key file not found" in result.output + result.stderr


def test_instance_url_required_for_token_mode(tmp_path: Path) -> None:
    result = _generate(tmp_path, "--access-token", "T")
    assert result.exit_code == 2
    assert "--instance-url" in result.output + result.stderr


def test_sf_failure_is_a_clean_error(tmp_path: Path, monkeypatch) -> None:
    def broken(alias):
        raise SfCliError("sf could not provide a session for 'acme': expired.")

    monkeypatch.setattr(cli_main, "org_credentials", broken)
    result = _generate(tmp_path, "--target-org", "acme")
    assert result.exit_code == 1
    assert "could not provide a session" in result.output + result.stderr
    assert "Traceback" not in result.output


# --------------------------------------------------------------------------- #
# Environment fallback
# --------------------------------------------------------------------------- #


def test_env_token_and_url_are_used_when_no_flag(
    tmp_path: Path, _offline: dict
) -> None:
    env = {"DATA360_ACCESS_TOKEN": "ENV-T", "DATA360_INSTANCE_URL": URL}
    result = _generate(tmp_path, env=env)
    assert result.exit_code == 0, result.output
    assert _offline["access_token"] == "ENV-T"


def test_env_target_org(tmp_path: Path, _offline: dict) -> None:
    result = _generate(tmp_path, env={"DATA360_TARGET_ORG": "acme"})
    assert result.exit_code == 0, result.output
    assert _offline["alias"] == "acme"


def test_flag_wins_over_env_without_conflict(tmp_path: Path, _offline: dict) -> None:
    # An exported token must not clash with an explicit --target-org.
    result = _generate(
        tmp_path, "--target-org", "acme", env={"DATA360_ACCESS_TOKEN": "ENV-T"}
    )
    assert result.exit_code == 0, result.output
    assert _offline["access_token"] == "SF-TOKEN"


def test_two_modes_in_env_are_rejected(tmp_path: Path) -> None:
    env = {"DATA360_TARGET_ORG": "acme", "DATA360_ACCESS_TOKEN": "T"}
    result = _generate(tmp_path, env=env)
    assert result.exit_code == 2


# --------------------------------------------------------------------------- #
# 401 hints, --verbose, --org-name
# --------------------------------------------------------------------------- #


def _reject(monkeypatch, exc: Exception) -> None:
    def fetch(**kwargs):
        raise exc

    monkeypatch.setattr(cli_main, "fetch_metadata", fetch)


def test_401_with_target_org_hints_sf_login_and_writes_nothing(
    tmp_path: Path, monkeypatch
) -> None:
    _reject(
        monkeypatch,
        MetadataUnauthorized(
            "Request rejected (401, INVALID_SESSION_ID) for /services/data/",
            detail="Request rejected (401) for https://acme.my.salesforce.com/...",
        ),
    )
    result = _generate(tmp_path, "--target-org", "acme")
    output = result.output + result.stderr
    assert result.exit_code == 1
    assert "sf org login web --alias acme" in output
    assert "acme.my.salesforce.com" not in output  # short, host-free by default
    assert list(tmp_path.iterdir()) == []


def test_401_with_access_token_hint(tmp_path: Path, monkeypatch) -> None:
    _reject(monkeypatch, MetadataUnauthorized("Request rejected (401)"))
    result = _generate(tmp_path, "--instance-url", URL, "--access-token", "T")
    assert result.exit_code == 1
    assert "access token was rejected" in result.output + result.stderr


def test_verbose_shows_full_detail(tmp_path: Path, monkeypatch) -> None:
    _reject(
        monkeypatch,
        MetadataError(
            "Request rejected (500) for /x",
            detail="Request rejected (500) for https://acme.my.salesforce.com/x: boom",
        ),
    )
    short = _generate(tmp_path, "--target-org", "acme")
    verbose = _generate(tmp_path, "--target-org", "acme", "--verbose")
    assert "boom" not in short.output + short.stderr
    assert "boom" in verbose.output + verbose.stderr


def test_org_name_sets_title_and_file_name(tmp_path: Path, _offline: dict) -> None:
    result = _generate(tmp_path, "--target-org", "acme", "--org-name", "Acme Demo")
    assert result.exit_code == 0, result.output
    assert _offline["org_name"] == "Acme Demo"
    assert (tmp_path / "acme-demo.json").exists()


def test_strict_is_passed_to_fetch(tmp_path: Path, _offline: dict) -> None:
    result = _generate(tmp_path, "--target-org", "acme", "--strict")
    assert result.exit_code == 0, result.output
    assert _offline["strict"] is True


def test_strict_failure_writes_nothing(tmp_path: Path, monkeypatch) -> None:
    _reject(
        monkeypatch,
        MetadataError(
            "1 of 2 DMO(s) could not be read; no snapshot written (--strict)."
        ),
    )
    result = _generate(tmp_path, "--target-org", "acme", "--strict")
    assert result.exit_code == 1
    assert "no snapshot written" in result.output + result.stderr
    assert list(tmp_path.iterdir()) == []


def test_diagram_image_is_written_and_listed(tmp_path: Path, monkeypatch) -> None:
    def fake_render(mmd_path, fmt):
        out = mmd_path.with_suffix(f".{fmt}")
        out.write_text("<svg/>", encoding="utf-8")
        return out

    monkeypatch.setattr(cli_main, "render_diagram_image", fake_render)
    result = _runner().invoke(
        cli_main.cli,
        [
            "generate",
            "--output",
            str(tmp_path),
            "--format",
            "markdown",
            "--target-org",
            "acme",
            "--org-name",
            "Acme",
            "--diagram-image",
            "svg",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "Wrote acme.svg" in result.output
    assert (tmp_path / "acme.svg").exists()


def test_missing_mmdc_warns_but_still_writes_docs(tmp_path: Path, monkeypatch) -> None:
    from data360_autodoc.generator.diagram_image import DiagramImageError

    def no_mmdc(mmd_path, fmt):
        raise DiagramImageError("mermaid-cli (mmdc) not found")

    monkeypatch.setattr(cli_main, "render_diagram_image", no_mmdc)
    result = _runner().invoke(
        cli_main.cli,
        [
            "generate",
            "--output",
            str(tmp_path),
            "--format",
            "markdown",
            "--target-org",
            "acme",
            "--org-name",
            "Acme",
            "--diagram-image",
            "png",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "Warning: mermaid-cli (mmdc) not found" in result.output + result.stderr
    assert (tmp_path / "acme.md").exists()


def test_diagram_image_needs_markdown_output(tmp_path: Path, _offline: dict) -> None:
    result = _generate(tmp_path, "--target-org", "acme", "--diagram-image", "svg")
    assert result.exit_code == 2  # _generate uses --format json
    assert "--format markdown or all" in result.output + result.stderr
    assert "alias" not in _offline  # rejected before signing in or fetching
