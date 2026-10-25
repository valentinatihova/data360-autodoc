"""Render the Mermaid diagram (``.mmd``) to an SVG or PNG image.

Some places docs end up, Confluence among them, do not render Mermaid. The
image is drawn by mermaid-cli (``mmdc``) when it is installed; data360-autodoc
does not bundle it (it pulls in a headless browser), so a missing ``mmdc`` is a
warning with an install hint, never a failed run.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Final

#: Image formats ``mmdc`` can write that make sense for documentation.
IMAGE_FORMATS: Final = ("svg", "png")

#: mmdc starts a headless browser; large diagrams can take a while.
MMDC_TIMEOUT_SECONDS: Final = 180

INSTALL_HINT: Final = "npm install --global @mermaid-js/mermaid-cli"


class DiagramImageError(RuntimeError):
    """The image could not be drawn; the message says why and what to do."""


def render_diagram_image(mmd_path: Path, image_format: str) -> Path:
    """Draw ``mmd_path`` as ``<same name>.<image_format>`` next to it.

    Raises:
        DiagramImageError: ``mmdc`` is missing, timed out or failed.
    """
    mmdc = shutil.which("mmdc")
    if mmdc is None:
        raise DiagramImageError(
            f"mermaid-cli (mmdc) not found, so no {image_format.upper()} was drawn. "
            f"Install it with `{INSTALL_HINT}` and run again."
        )
    out_path = mmd_path.with_suffix(f".{image_format}")
    try:
        completed = subprocess.run(
            [mmdc, "-i", str(mmd_path), "-o", str(out_path), "-b", "white"],
            capture_output=True,
            text=True,
            timeout=MMDC_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise DiagramImageError(
            f"mmdc did not finish within {MMDC_TIMEOUT_SECONDS} s."
        ) from exc
    except OSError as exc:
        raise DiagramImageError(f"Could not run mmdc: {exc.strerror or exc}") from exc
    if completed.returncode != 0 or not out_path.exists():
        lines = (completed.stderr or completed.stdout or "").strip().splitlines()
        raise DiagramImageError(
            f"mmdc failed: {lines[-1] if lines else f'exit {completed.returncode}'}"
        )
    return out_path
