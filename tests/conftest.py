"""Shared pytest fixtures for the mock-based fetcher tests."""

from __future__ import annotations

from pathlib import Path

import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


@pytest.fixture(scope="session")
def rsa_private_key_pem() -> str:
    """Return a freshly generated RSA private key in PEM format (test-only)."""
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode("utf-8")


@pytest.fixture
def private_key_path(tmp_path: Path, rsa_private_key_pem: str) -> str:
    """Write the test private key to a temp .pem file and return its path."""
    key_file = tmp_path / "server.pem"
    key_file.write_text(rsa_private_key_pem, encoding="utf-8")
    return str(key_file)


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    """Neutralize backoff sleeps so retry tests run instantly."""
    monkeypatch.setattr("time.sleep", lambda *_args, **_kwargs: None)
