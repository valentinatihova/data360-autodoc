"""Tests for the drift report renderers and the ``diff`` CLI command."""

from __future__ import annotations

import json
import shutil
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

import pytest
from click.testing import CliRunner

from data360_autodoc.cli.main import EXIT_DRIFT, EXIT_ERROR, cli
from data360_autodoc.diff import diff_schemas
from data360_autodoc.generator.drift import (
    DIFF_REPORT_VERSION,
    render_diff_json,
    render_diff_markdown,
)
from data360_autodoc.generator.snapshot import load_json
from data360_autodoc.models import (
    DataModelObject,
    DataStream,
    FieldDef,
    FieldMapping,
    OrgSchema,
)

FIXTURES = Path(__file__).parent / "fixtures"
BEFORE = str(FIXTURES / "acme-before.json")
AFTER = str(FIXTURES / "acme-after.json")


def _runner() -> CliRunner:
    """A runner that keeps stderr apart from stdout on every supported Click.

    Click >= 8.2 always separates them; 8.1 needs ``mix_stderr=False``.
    """
    try:
        return CliRunner(mix_stderr=False)
    except TypeError:
        return CliRunner()


def _fixture_diff():
    def load(path: str) -> OrgSchema:
        return load_json(Path(path).read_text(encoding="utf-8"))

    return diff_schemas(load(BEFORE), load(AFTER))


# --------------------------------------------------------------------------- #
# Markdown
# --------------------------------------------------------------------------- #


def test_markdown_header_and_summary() -> None:
    md = render_diff_markdown(_fixture_diff())
    assert md.startswith("# Data 360 Schema Drift — Acme Data Cloud\n")
    assert "_Old: 2026-10-01 06:00:00 UTC · https://acme.my.salesforce.com_" in md
    assert "_New: 2026-10-08 06:00:00 UTC · https://acme.my.salesforce.com_" in md
    assert "**18 changes detected.**" in md
    assert "| DMO fields | 2 | 0 | 1 |" in md
    assert "| DLO → DMO field mappings | 4 | 1 | — |" in md


def test_markdown_sections() -> None:
    md = render_diff_markdown(_fixture_diff())
    assert "- Account (`ssot__Account__dlm`) — 2 fields" in md
    assert "- Legacy Leads (`Legacy_Leads__dll`) — 1 field" in md
    assert "| changed | ssot__TotalAmount__c | type: Text → Number |" in md
    assert "| added | ssot__BirthDate__c | Date |" in md
    assert "| removed | Legacy_Leads__dll | ssot__Individual__dlm |" in md
    assert (
        "| removed | Legacy_Leads__dll | LeadId | ssot__Individual__dlm "
        "| ssot__Id__c |" in md
    )
    assert "| status: ACTIVE → INACTIVE |" in md
    assert "| N:1, ACTIVE |" in md


def test_markdown_no_drift() -> None:
    snapshot = load_json(Path(AFTER).read_text(encoding="utf-8"))
    md = render_diff_markdown(diff_schemas(snapshot, snapshot))
    assert "**No schema drift detected.**" in md
    assert "## " not in md


def test_markdown_escapes_org_text_and_shows_key_changes() -> None:
    ts = datetime(2026, 10, 1, tzinfo=timezone.utc)
    old = OrgSchema(
        org_name="A|B",
        instance_url="https://x",
        generated_at=ts,
        dmos=(DataModelObject("X__dmo", "X", (FieldDef("Id__c", "Text"),)),),
    )
    new = OrgSchema(
        org_name="A|B",
        instance_url="https://x",
        generated_at=ts,
        dmos=(
            DataModelObject(
                "X__dmo",
                "X|Y",
                (FieldDef("Id__c", "Text", is_key=True, key_qualifier="PK"),),
            ),
        ),
    )
    md = render_diff_markdown(diff_schemas(old, new))
    assert "Drift — A\\|B" in md
    assert "- label: X → X\\|Y" in md
    assert "| changed | Id__c | is_key: no → yes; key_qualifier: ∅ → PK |" in md


def test_streams_in_markdown_and_json() -> None:
    ts = datetime(2026, 10, 1, tzinfo=timezone.utc)
    stream = DataStream("Orders", "Order_Home__dll", "Order (Home)")
    field = FieldMapping("Orders", "Amt", "Amount", "Amount__c", "Text")
    old = OrgSchema("A", "https://x", ts, streams=(stream,), field_mappings=(field,))
    new = OrgSchema(
        "A",
        "https://x",
        ts,
        streams=(replace(stream, primary_keys=("OrderId", "Line")),),
        field_mappings=(replace(field, data_type="Number"),),
    )
    diff = diff_schemas(old, new)
    md = render_diff_markdown(diff)
    assert "| Data streams | 0 | 0 | 1 |" in md
    assert "| changed | Orders | primary_keys: ∅ → OrderId, Line |" in md
    assert "| changed | Orders | Amount__c | data_type: Text → Number |" in md
    data = json.loads(render_diff_json(diff))
    assert data["streams"]["changed"] == [
        {
            "name": "Orders",
            "changes": [
                {"attribute": "primary_keys", "old": [], "new": ["OrderId", "Line"]}
            ],
        }
    ]
    assert data["stream_fields"]["changed"][0]["dlo_field_name"] == "Amount__c"


def test_markdown_header_names_both_orgs_when_they_differ() -> None:
    ts = datetime(2026, 10, 1, tzinfo=timezone.utc)
    prod = OrgSchema("Acme Production", "https://acme.my.salesforce.com", ts)
    sandbox = replace(prod, org_name="Acme Sandbox")
    md = render_diff_markdown(diff_schemas(prod, sandbox))
    assert md.startswith("# Data 360 Schema Drift — Acme Production → Acme Sandbox\n")


def test_scope_warning_in_markdown_json_and_cli(tmp_path: Path) -> None:
    data = json.loads(Path(AFTER).read_text(encoding="utf-8"))
    old, new = tmp_path / "old.json", tmp_path / "new.json"
    old.write_text(json.dumps({**data, "dmo_scope": "all"}), encoding="utf-8")
    new.write_text(json.dumps({**data, "dmo_scope": "enabled"}), encoding="utf-8")
    result = _runner().invoke(cli, ["diff", str(old), str(new)])
    assert result.exit_code == 0, result.output
    assert "> ⚠️ Snapshots cover different DMO scopes" in result.stdout
    assert "Warning: Snapshots cover different DMO scopes" in result.stderr
    json_result = _runner().invoke(
        cli, ["diff", str(old), str(new), "--format", "json"]
    )
    assert json.loads(json_result.stdout)["warnings"]


def test_markdown_is_deterministic() -> None:
    assert render_diff_markdown(_fixture_diff()) == render_diff_markdown(
        _fixture_diff()
    )


# --------------------------------------------------------------------------- #
# JSON
# --------------------------------------------------------------------------- #


def test_json_report_shape() -> None:
    data = json.loads(render_diff_json(_fixture_diff()))
    assert data["diff_report_version"] == DIFF_REPORT_VERSION
    assert data["has_changes"] is True
    assert data["change_count"] == 18
    assert data["old"]["generated_at"] == "2026-10-01T06:00:00+00:00"
    assert [o["name"] for o in data["dmos"]["added"]] == ["ssot__Account__dlm"]
    sales_order = next(
        c for c in data["dmos"]["changed"] if c["name"] == "ssot__SalesOrder__dlm"
    )
    assert sales_order["fields"]["changed"] == [
        {
            "name": "ssot__TotalAmount__c",
            "changes": [{"attribute": "type", "old": "Text", "new": "Number"}],
        }
    ]
    assert data["mappings"]["removed"] == [
        {"source_dlo": "Legacy_Leads__dll", "target_dmo": "ssot__Individual__dlm"}
    ]
    (rel,) = data["relationships"]["changed"]
    assert rel["changes"] == [
        {"attribute": "status", "old": "ACTIVE", "new": "INACTIVE"}
    ]


def test_json_no_drift() -> None:
    snapshot = load_json(Path(AFTER).read_text(encoding="utf-8"))
    data = json.loads(render_diff_json(diff_schemas(snapshot, snapshot)))
    assert data["has_changes"] is False
    assert data["change_count"] == 0


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def test_cli_diff_markdown_to_stdout() -> None:
    result = _runner().invoke(cli, ["diff", BEFORE, AFTER])
    assert result.exit_code == 0, result.output
    assert "# Data 360 Schema Drift — Acme Data Cloud" in result.stdout
    assert "Schema drift: 18 changes" in result.stderr
    assert "Schema drift:" not in result.stdout


def test_cli_diff_json_stdout_is_pure_json() -> None:
    result = _runner().invoke(cli, ["diff", BEFORE, AFTER, "--format", "json"])
    assert result.exit_code == 0, result.output
    assert json.loads(result.stdout)["change_count"] == 18


def test_cli_fail_on_change_exits_nonzero_on_drift() -> None:
    result = _runner().invoke(cli, ["diff", BEFORE, AFTER, "--fail-on-change"])
    assert result.exit_code == EXIT_DRIFT


def test_cli_fail_on_change_exits_zero_without_drift() -> None:
    result = _runner().invoke(cli, ["diff", AFTER, AFTER, "--fail-on-change"])
    assert result.exit_code == 0, result.output
    assert "No schema drift." in result.stderr


def test_cli_output_file(tmp_path: Path) -> None:
    out = tmp_path / "reports" / "drift.md"
    result = _runner().invoke(cli, ["diff", BEFORE, AFTER, "--output", str(out)])
    assert result.exit_code == 0, result.output
    assert "Wrote drift.md" in result.stdout
    assert out.read_text(encoding="utf-8").startswith("# Data 360 Schema Drift")


def test_cli_report_file_written_even_when_failing(tmp_path: Path) -> None:
    # CI uploads/posts the report after the step fails, so it must exist.
    out = tmp_path / "drift.json"
    result = _runner().invoke(
        cli,
        ["diff", BEFORE, AFTER, "--format", "json", "--output", str(out)]
        + ["--fail-on-change"],
    )
    assert result.exit_code == EXIT_DRIFT
    assert json.loads(out.read_text(encoding="utf-8"))["has_changes"] is True


@pytest.mark.parametrize(
    "content,expected",
    [
        ("not json", "Could not read snapshot"),
        ('{"org_name": "x"}', "missing required key 'instance_url'"),
        ("[]", "Could not read snapshot"),
    ],
)
def test_cli_unreadable_snapshot_is_clean_error(
    tmp_path: Path, content: str, expected: str
) -> None:
    bad = tmp_path / "bad.json"
    bad.write_text(content, encoding="utf-8")
    result = _runner().invoke(cli, ["diff", str(bad), AFTER])
    assert result.exit_code == EXIT_ERROR
    assert expected in result.stderr
    assert "Traceback" not in result.stderr


def test_cli_future_snapshot_version_is_clean_error(tmp_path: Path) -> None:
    data = json.loads(Path(AFTER).read_text(encoding="utf-8"))
    data["snapshot_version"] = 999
    future = tmp_path / "future.json"
    future.write_text(json.dumps(data), encoding="utf-8")
    result = _runner().invoke(cli, ["diff", BEFORE, str(future)])
    assert result.exit_code == EXIT_ERROR
    assert "Unsupported snapshot_version 999" in result.stderr


def test_cli_malformed_snapshot_is_error_not_drift(tmp_path: Path) -> None:
    # Valid JSON with a null name must not crash with exit 1 (= drift).
    data = json.loads(Path(AFTER).read_text(encoding="utf-8"))
    data["dmos"][0]["name"] = None
    bad = tmp_path / "null-name.json"
    bad.write_text(json.dumps(data), encoding="utf-8")
    result = _runner().invoke(cli, ["diff", BEFORE, str(bad), "--fail-on-change"])
    assert result.exit_code == EXIT_ERROR
    assert "Malformed snapshot data" in result.stderr


def test_cli_unwritable_output_is_error_not_drift(tmp_path: Path) -> None:
    blocker = tmp_path / "file"
    blocker.write_text("", encoding="utf-8")
    out = blocker / "drift.md"  # parent is a file
    result = _runner().invoke(
        cli, ["diff", BEFORE, AFTER, "--output", str(out), "--fail-on-change"]
    )
    assert result.exit_code == EXIT_ERROR
    assert "Could not write report" in result.stderr


def test_cli_missing_file_is_usage_error(tmp_path: Path) -> None:
    result = _runner().invoke(cli, ["diff", BEFORE, str(tmp_path / "nope.json")])
    assert result.exit_code == 2
    assert "does not exist" in result.stderr


def test_cli_diff_does_not_need_org_credentials(tmp_path: Path) -> None:
    # Pure file comparison: works on copies anywhere, no auth flags involved.
    old, new = tmp_path / "a.json", tmp_path / "b.json"
    shutil.copy(BEFORE, old)
    shutil.copy(AFTER, new)
    result = _runner().invoke(cli, ["diff", str(old), str(new)])
    assert result.exit_code == 0, result.output
