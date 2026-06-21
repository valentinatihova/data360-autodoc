"""Tests for the Mermaid generator."""

from __future__ import annotations

from datetime import datetime, timezone

from generator.mermaid import render_mermaid
from models import DataLakeObject, DataModelObject, Mapping, OrgSchema

FIXED_TS = datetime(2026, 6, 21, 17, 30, 0, tzinfo=timezone.utc)


def _schema(**kwargs) -> OrgSchema:
    base = dict(
        org_name="Acme",
        instance_url="https://acme.my.salesforce.com",
        generated_at=FIXED_TS,
    )
    base.update(kwargs)
    return OrgSchema(**base)


def test_basic_graph_with_labels() -> None:
    schema = _schema(
        dlos=(DataLakeObject(name="Order_Home__dll", label="Order (Home)"),),
        dmos=(DataModelObject(name="Individual__dmo", label="Individual"),),
        mappings=(Mapping(source_dlo="Order_Home__dll", target_dmo="Individual__dmo"),),
    )
    out = render_mermaid(schema)
    assert out.startswith("graph LR\n")
    # Label looked up from the schema, parens preserved inside quotes.
    assert 'Order_Home__dll["Order (Home)"]' in out
    assert 'Individual__dmo["Individual"]' in out
    assert "  Order_Home__dll --> Individual__dmo" in out


def test_no_mappings_emits_valid_placeholder() -> None:
    out = render_mermaid(_schema())
    assert out == 'graph LR\n  no_mappings["No DLO to DMO mappings found"]'


def test_orphan_mapping_falls_back_to_name() -> None:
    # Mapping references a DMO not in the schema -> label falls back to name.
    schema = _schema(
        dlos=(DataLakeObject(name="Order_Home__dll", label="Order (Home)"),),
        mappings=(Mapping(source_dlo="Order_Home__dll", target_dmo="Ghost__dmo"),),
    )
    out = render_mermaid(schema)
    assert 'Ghost__dmo["Ghost__dmo"]' in out


def test_label_quotes_and_brackets_are_neutralized() -> None:
    schema = _schema(
        dlos=(DataLakeObject(name="Weird__dll", label='Has "quotes" [and] brackets'),),
        dmos=(DataModelObject(name="Target__dmo", label="Target"),),
        mappings=(Mapping(source_dlo="Weird__dll", target_dmo="Target__dmo"),),
    )
    out = render_mermaid(schema)
    assert "Has 'quotes' (and) brackets" in out
    assert '"quotes"' not in out.replace('["', "").replace('"]', "")


def test_each_node_declared_once() -> None:
    # Two mappings sharing the same DMO -> the DMO node is declared a single time.
    schema = _schema(
        dlos=(
            DataLakeObject(name="A__dll", label="A"),
            DataLakeObject(name="B__dll", label="B"),
        ),
        dmos=(DataModelObject(name="Shared__dmo", label="Shared"),),
        mappings=(
            Mapping(source_dlo="A__dll", target_dmo="Shared__dmo"),
            Mapping(source_dlo="B__dll", target_dmo="Shared__dmo"),
        ),
    )
    out = render_mermaid(schema)
    assert out.count('Shared__dmo["Shared"]') == 1
    assert "  A__dll --> Shared__dmo" in out
    assert "  B__dll --> Shared__dmo" in out


def test_deterministic_output() -> None:
    schema = _schema(
        dlos=(DataLakeObject(name="Order_Home__dll", label="Order"),),
        dmos=(DataModelObject(name="Individual__dmo", label="Individual"),),
        mappings=(Mapping(source_dlo="Order_Home__dll", target_dmo="Individual__dmo"),),
    )
    assert render_mermaid(schema) == render_mermaid(schema)
