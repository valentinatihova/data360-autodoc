"""Tests for borrowing an org session from the Salesforce CLI (sf is mocked)."""

from __future__ import annotations

import json
import subprocess

import pytest

from data360_autodoc.fetcher import sf_cli

TOKEN = "00Dxx!SECRET-TOKEN"


def _sf(monkeypatch, *, stdout: str = "", returncode: int = 0, raises=None) -> list:
    calls: list = []
    monkeypatch.setattr(sf_cli.shutil, "which", lambda name: "/usr/local/bin/sf")

    def fake_run(args, **kwargs):
        calls.append(args)
        if raises:
            raise raises
        return subprocess.CompletedProcess(args, returncode, stdout=stdout, stderr="")

    monkeypatch.setattr(sf_cli.subprocess, "run", fake_run)
    return calls


def _ok_json() -> str:
    return json.dumps(
        {
            "status": 0,
            "result": {
                "instanceUrl": "https://acme.my.salesforce.com",
                "accessToken": TOKEN,
            },
        }
    )


def test_returns_url_and_token_even_after_warning_lines(monkeypatch) -> None:
    calls = _sf(monkeypatch, stdout=" ›   Warning: update available\n" + _ok_json())
    assert sf_cli.org_credentials("acme") == ("https://acme.my.salesforce.com", TOKEN)
    assert calls == [
        ["/usr/local/bin/sf", "org", "display", "--target-org", "acme", "--json"]
    ]


def test_sf_not_installed(monkeypatch) -> None:
    monkeypatch.setattr(sf_cli.shutil, "which", lambda name: None)
    with pytest.raises(sf_cli.SfCliError, match="not found on PATH"):
        sf_cli.org_credentials("acme")


def test_unknown_alias_shows_sf_message_and_login_hint(monkeypatch) -> None:
    body = {"status": 1, "message": "No authorization information found for acme."}
    _sf(monkeypatch, stdout=json.dumps(body), returncode=1)
    with pytest.raises(sf_cli.SfCliError) as exc:
        sf_cli.org_credentials("acme")
    assert "No authorization information found" in str(exc.value)
    assert "sf org login web --alias acme" in str(exc.value)


def test_timeout(monkeypatch) -> None:
    _sf(monkeypatch, raises=subprocess.TimeoutExpired("sf", 60))
    with pytest.raises(sf_cli.SfCliError, match="did not answer"):
        sf_cli.org_credentials("acme")


def test_output_without_token(monkeypatch) -> None:
    body = {"status": 0, "result": {"instanceUrl": "https://acme.my.salesforce.com"}}
    _sf(monkeypatch, stdout=json.dumps(body))
    with pytest.raises(sf_cli.SfCliError, match="no access token"):
        sf_cli.org_credentials("acme")


def test_non_json_output(monkeypatch) -> None:
    _sf(monkeypatch, stdout="something went wrong", returncode=1)
    with pytest.raises(sf_cli.SfCliError, match="no access token"):
        sf_cli.org_credentials("acme")


def test_token_never_appears_in_errors(monkeypatch) -> None:
    # Even when sf exits non-zero after printing a session, the token stays out.
    _sf(monkeypatch, stdout=_ok_json(), returncode=1)
    with pytest.raises(sf_cli.SfCliError) as exc:
        sf_cli.org_credentials("acme")
    assert TOKEN not in str(exc.value)


def test_redacted_token_is_fetched_with_show_access_token(monkeypatch) -> None:
    # sf 2.15x+ prints "[REDACTED] Use 'sf org auth show-access-token' to view".
    display = {
        "status": 0,
        "result": {
            "instanceUrl": "https://acme.my.salesforce.com",
            "accessToken": "[REDACTED] Use 'sf org auth show-access-token' to view",
        },
    }
    shown = {"status": 0, "result": {"accessToken": TOKEN}}
    outputs = iter([json.dumps(display), json.dumps(shown)])
    calls: list = []
    monkeypatch.setattr(sf_cli.shutil, "which", lambda name: "/usr/local/bin/sf")

    def fake_run(args, **kwargs):
        calls.append(args)
        return subprocess.CompletedProcess(args, 0, stdout=next(outputs), stderr="")

    monkeypatch.setattr(sf_cli.subprocess, "run", fake_run)
    assert sf_cli.org_credentials("acme") == ("https://acme.my.salesforce.com", TOKEN)
    assert calls[1] == [
        "/usr/local/bin/sf",
        "org",
        "auth",
        "show-access-token",
        "--target-org",
        "acme",
        "--json",
    ]


def test_still_redacted_is_an_error_not_a_token(monkeypatch) -> None:
    body = {
        "status": 0,
        "result": {
            "instanceUrl": "https://acme.my.salesforce.com",
            "accessToken": "[REDACTED] Use 'sf org auth show-access-token' to view",
        },
    }
    _sf(monkeypatch, stdout=json.dumps(body))
    with pytest.raises(sf_cli.SfCliError, match="no access token"):
        sf_cli.org_credentials("acme")
