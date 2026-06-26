"""Mock tests for the JWT bearer auth flow."""

from __future__ import annotations

import jwt
import pytest
import responses

from data360_autodoc.fetcher import auth

INSTANCE_URL = "https://example.my.salesforce.com"
# get_access_token defaults to the production login host, not the instance URL.
TOKEN_URL = auth.DEFAULT_TOKEN_URL


def _params() -> dict[str, str]:
    return {
        "instance_url": INSTANCE_URL,
        "client_id": "3MVG9abc",
        "username": "admin@example.com",
    }


def test_build_assertion_roundtrips_claims(rsa_private_key_pem: str) -> None:
    token = auth.build_assertion(
        client_id="3MVG9abc",
        username="admin@example.com",
        private_key=rsa_private_key_pem,
        audience=auth.AUD_SANDBOX,
        now=1_000_000,
    )
    # Decode without verifying the signature (we only assert claim contents).
    claims = jwt.decode(token, options={"verify_signature": False})
    assert claims["iss"] == "3MVG9abc"
    assert claims["sub"] == "admin@example.com"
    assert claims["aud"] == auth.AUD_SANDBOX
    assert claims["exp"] == 1_000_000 + 180


@responses.activate
def test_get_access_token_success(private_key_path: str) -> None:
    responses.add(
        responses.POST,
        TOKEN_URL,
        json={"access_token": "TOKEN123", "instance_url": INSTANCE_URL},
        status=200,
    )
    result = auth.get_access_token(private_key_path=private_key_path, **_params())
    assert result == {"access_token": "TOKEN123", "instance_url": INSTANCE_URL}
    assert len(responses.calls) == 1


@responses.activate
def test_get_access_token_prefers_returned_instance_url(
    private_key_path: str,
) -> None:
    responses.add(
        responses.POST,
        TOKEN_URL,
        json={
            "access_token": "TOKEN123",
            "instance_url": "https://eu.my.salesforce.com",
        },
        status=200,
    )
    result = auth.get_access_token(private_key_path=private_key_path, **_params())
    assert result["instance_url"] == "https://eu.my.salesforce.com"


@responses.activate
def test_get_access_token_retries_then_succeeds(private_key_path: str) -> None:
    responses.add(responses.POST, TOKEN_URL, status=503)
    responses.add(responses.POST, TOKEN_URL, status=500)
    responses.add(
        responses.POST,
        TOKEN_URL,
        json={"access_token": "TOKEN123", "instance_url": INSTANCE_URL},
        status=200,
    )
    result = auth.get_access_token(private_key_path=private_key_path, **_params())
    assert result["access_token"] == "TOKEN123"
    assert len(responses.calls) == 3


@responses.activate
def test_get_access_token_4xx_is_terminal(private_key_path: str) -> None:
    responses.add(
        responses.POST,
        TOKEN_URL,
        json={"error": "invalid_grant"},
        status=400,
    )
    with pytest.raises(auth.AuthError):
        auth.get_access_token(private_key_path=private_key_path, **_params())
    # No retry on a client error.
    assert len(responses.calls) == 1


@responses.activate
def test_get_access_token_gives_up_after_three(private_key_path: str) -> None:
    for _ in range(3):
        responses.add(responses.POST, TOKEN_URL, status=502)
    with pytest.raises(auth.AuthError):
        auth.get_access_token(private_key_path=private_key_path, **_params())
    assert len(responses.calls) == 3


def test_get_access_token_missing_key_file() -> None:
    with pytest.raises(FileNotFoundError):
        auth.get_access_token(private_key_path="/no/such/key.pem", **_params())


@responses.activate
def test_get_access_token_sandbox_token_url(private_key_path: str) -> None:
    responses.add(
        responses.POST,
        auth.SANDBOX_TOKEN_URL,
        json={"access_token": "TOKEN123", "instance_url": INSTANCE_URL},
        status=200,
    )
    result = auth.get_access_token(
        private_key_path=private_key_path,
        token_url=auth.SANDBOX_TOKEN_URL,
        audience=auth.AUD_SANDBOX,
        **_params(),
    )
    assert result["access_token"] == "TOKEN123"
    assert responses.calls[0].request.url == auth.SANDBOX_TOKEN_URL


@responses.activate
def test_get_access_token_missing_access_token_raises(private_key_path: str) -> None:
    # 200 OK but the body has no access_token (misbehaving endpoint).
    responses.add(
        responses.POST,
        TOKEN_URL,
        json={"instance_url": INSTANCE_URL},
        status=200,
    )
    with pytest.raises(auth.AuthError, match="access_token not found"):
        auth.get_access_token(private_key_path=private_key_path, **_params())
