"""Unit tests for the shared HTTP layer (fetcher/_http)."""

from __future__ import annotations

import pytest
import responses

from data360_autodoc.fetcher._http import FetchError, get_json

URL = "https://example.my.salesforce.com/services/data/"


@responses.activate
def test_non_json_200_becomes_fetch_error() -> None:
    # 200 with an HTML body (e.g. a proxy/login page) must not leak a raw
    # JSONDecodeError — it becomes a FetchError the orchestrator can funnel.
    responses.add(
        responses.GET,
        URL,
        body="<html>not json</html>",
        status=200,
        content_type="text/html",
    )
    with pytest.raises(FetchError, match="Non-JSON"):
        get_json(URL, access_token="TOK", timeout=5.0)
