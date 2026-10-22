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


@responses.activate
def test_204_no_content_is_an_empty_result_not_retried() -> None:
    # Data 360 answers a DMO with no relationships with 204 No Content.
    responses.add(responses.GET, URL, status=204)
    assert get_json(URL, access_token="TOK", timeout=5) == {}
    assert len(responses.calls) == 1


@responses.activate
def test_401_is_unauthorized_with_short_host_free_message() -> None:
    from data360_autodoc.fetcher._http import UnauthorizedError

    body = '[{"errorCode":"INVALID_SESSION_ID","message":"Session expired"}]'
    responses.add(responses.GET, URL, body=body, status=401)
    with pytest.raises(UnauthorizedError) as exc:
        get_json(URL + "?dmoDeveloperName=Secret__dlm", access_token="TOK", timeout=5)
    assert str(exc.value) == (
        "Request rejected (401, INVALID_SESSION_ID) for /services/data/"
    )
    assert "example.my.salesforce.com" in exc.value.detail
    assert len(responses.calls) == 1  # 4xx is never retried


@responses.activate
def test_retry_exhausted_message_is_short(monkeypatch) -> None:
    from data360_autodoc.fetcher import _http

    monkeypatch.setattr(_http.time, "sleep", lambda s: None)
    responses.add(responses.GET, URL, body="upstream exploded", status=503)
    with pytest.raises(FetchError) as exc:
        get_json(URL, access_token="TOK", timeout=5)
    assert str(exc.value) == (
        "Request to /services/data/ failed after 3 attempts: HTTP 503"
    )
    assert "upstream exploded" in exc.value.detail
