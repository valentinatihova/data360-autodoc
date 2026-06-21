"""Mermaid diagram generator for a Data 360 org.

Pure function of :class:`~models.OrgSchema` -> a ``graph LR`` Mermaid string
showing DLO -> DMO mappings.

Node identity is split from display text so arbitrary org labels can never
break Mermaid syntax:

- **Node ID** is derived from the API name, sanitized to ``[A-Za-z0-9_]`` and
  prefixed if it would otherwise start with a digit. Stable and collision-safe
  for Salesforce API names.
- **Display label** is the human label (looked up from the schema), wrapped in
  quotes with quote/bracket characters neutralized.

Example output::

    graph LR
      Order_Home__dll["Order (Home)"] --> Individual__dmo["Individual"]
"""

from __future__ import annotations

import re

from models import OrgSchema

_UNSAFE_ID = re.compile(r"[^A-Za-z0-9_]")


def render_mermaid(schema: OrgSchema) -> str:
    """Render an :class:`~models.OrgSchema` as a Mermaid ``graph LR`` string.

    Builds DLO -> DMO edges from ``schema.mappings``, resolving display labels
    from the DLO/DMO catalogs (falling back to the API name for any mapping
    endpoint not present in the schema). Deterministic: ``mappings`` is already
    sorted, so node and edge order are stable.

    Args:
        schema: The normalized org snapshot to diagram.

    Returns:
        A Mermaid diagram string. When there are no mappings, returns a valid
        single-node diagram noting their absence (never broken syntax).
    """
    label_by_name = _build_label_index(schema)

    if not schema.mappings:
        return "graph LR\n" '  no_mappings["No DLO to DMO mappings found"]'

    lines = ["graph LR"]
    declared: set[str] = set()
    node_decls: list[str] = []
    edges: list[str] = []

    for mapping in schema.mappings:
        src_id = _node_id(mapping.source_dlo)
        dst_id = _node_id(mapping.target_dmo)
        # Declare each unique node once, in first-seen (sorted) order.
        for node_id, name in (
            (src_id, mapping.source_dlo),
            (dst_id, mapping.target_dmo),
        ):
            if node_id not in declared:
                declared.add(node_id)
                label = label_by_name.get(name, name)
                node_decls.append(f'  {node_id}["{_escape_label(label)}"]')
        edges.append(f"  {src_id} --> {dst_id}")

    lines.extend(node_decls)
    lines.extend(edges)
    return "\n".join(lines)


def _build_label_index(schema: OrgSchema) -> dict[str, str]:
    """Map API name -> display label for every DLO and DMO in the schema."""
    index: dict[str, str] = {}
    for obj in schema.dlos:
        index[obj.name] = obj.label
    for obj in schema.dmos:
        index[obj.name] = obj.label
    return index


def _node_id(name: str) -> str:
    """Derive a Mermaid-safe node ID from an API name.

    Replaces any character outside ``[A-Za-z0-9_]`` with an underscore and
    prefixes a leading digit so the ID is always a valid Mermaid identifier.
    """
    safe = _UNSAFE_ID.sub("_", name)
    if safe and safe[0].isdigit():
        safe = f"n_{safe}"
    return safe or "node"


def _escape_label(label: str) -> str:
    """Neutralize characters that break a quoted Mermaid label.

    Double quotes would close the label early; square brackets confuse the
    node-shape parser; newlines break the line. Everything else (spaces,
    parens, slashes) is safe inside the quotes.
    """
    return (
        label.replace('"', "'")
        .replace("[", "(")
        .replace("]", ")")
        .replace("\r\n", " ")
        .replace("\n", " ")
        .replace("\r", " ")
    )
