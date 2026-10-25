"""Tests for drawing the Mermaid diagram as SVG/PNG (mmdc is mocked)."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from data360_autodoc.generator import diagram_image as di


@pytest.fixture
def mmd(tmp_path: Path) -> Path:
    path = tmp_path / "acme.mmd"
    path.write_text("graph LR\n  A --> B\n", encoding="utf-8")
    return path


def _mmdc(monkeypatch, *, returncode: int = 0, stderr: str = "", writes: bool = True):
    calls: list = []
    monkeypatch.setattr(di.shutil, "which", lambda name: "/usr/local/bin/mmdc")

    def fake_run(args, **kwargs):
        calls.append(args)
        if writes:
            Path(args[args.index("-o") + 1]).write_text("<svg/>", encoding="utf-8")
        return subprocess.CompletedProcess(args, returncode, stdout="", stderr=stderr)

    monkeypatch.setattr(di.subprocess, "run", fake_run)
    return calls


@pytest.mark.parametrize("fmt", ["svg", "png"])
def test_draws_next_to_the_mmd(monkeypatch, mmd: Path, fmt: str) -> None:
    calls = _mmdc(monkeypatch)
    out = di.render_diagram_image(mmd, fmt)
    assert out == mmd.with_suffix(f".{fmt}")
    assert out.exists()
    assert calls[0][:5] == ["/usr/local/bin/mmdc", "-i", str(mmd), "-o", str(out)]


def test_missing_mmdc_gives_install_hint(monkeypatch, mmd: Path) -> None:
    monkeypatch.setattr(di.shutil, "which", lambda name: None)
    with pytest.raises(di.DiagramImageError, match="npm install --global"):
        di.render_diagram_image(mmd, "svg")


def test_mmdc_failure_reports_its_last_line(monkeypatch, mmd: Path) -> None:
    _mmdc(monkeypatch, returncode=1, stderr="Parse error\nbad arrow", writes=False)
    with pytest.raises(di.DiagramImageError, match="mmdc failed: bad arrow"):
        di.render_diagram_image(mmd, "png")


def test_timeout(monkeypatch, mmd: Path) -> None:
    monkeypatch.setattr(di.shutil, "which", lambda name: "/usr/local/bin/mmdc")

    def slow(args, **kwargs):
        raise subprocess.TimeoutExpired("mmdc", 180)

    monkeypatch.setattr(di.subprocess, "run", slow)
    with pytest.raises(di.DiagramImageError, match="did not finish"):
        di.render_diagram_image(mmd, "svg")
