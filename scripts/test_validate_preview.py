#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml", "pytest"]
# ///
"""Tests for validate_preview.py.

Run with:  uv run scripts/test_validate_preview.py
"""

import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).with_name("validate_preview.py")

STORE = "bitwarden-secretsmanager"
PLACEHOLDER = "<preview-url>"

INGRESS = """\
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: n8n
spec:
  rules:
    - host: {host}
  tls:
    - hosts:
        - {host}
"""

HTTPROUTE = """\
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: n8n-webhooks
spec:
  hostnames:
    - {host}
"""

EXTERNAL_SECRET = """\
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  name: n8n-env
spec:
  secretStoreRef:
    name: {store}
    kind: ClusterSecretStore
"""


def _run(stdin: str):
    result = subprocess.run(
        [
            sys.executable, str(SCRIPT),
            "--secret-store", STORE,
            "--placeholder", PLACEHOLDER,
        ],
        input=stdin,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stderr


def test_valid_manifest_passes():
    manifest = (
        INGRESS.format(host="<preview-url>.services.sbling.net")
        + "---\n"
        + HTTPROUTE.format(host="<preview-url>.sbling.net")
        + "---\n"
        + EXTERNAL_SECRET.format(store="bitwarden-preview")
    )
    rc, stderr = _run(manifest)
    assert rc == 0
    assert stderr == ""


def test_production_secret_store_is_rejected():
    rc, stderr = _run(EXTERNAL_SECRET.format(store="bitwarden-secretsmanager"))
    assert rc == 1
    assert "n8n-env" in stderr and "bitwarden-secretsmanager" in stderr


def test_non_placeholder_ingress_host_is_rejected():
    rc, stderr = _run(INGRESS.format(host="n8n.services.sbling.net"))
    assert rc == 1
    assert "n8n.services.sbling.net" in stderr


def test_non_placeholder_route_host_is_rejected():
    rc, stderr = _run(HTTPROUTE.format(host="webhooks.sbling.net"))
    assert rc == 1
    assert "webhooks.sbling.net" in stderr


def test_headless_app_passes():
    # No Ingress/HTTPRoute and an overridden store is valid.
    rc, stderr = _run(EXTERNAL_SECRET.format(store="preview-store"))
    assert rc == 0
    assert stderr == ""


def test_all_failures_are_reported():
    manifest = (
        INGRESS.format(host="n8n.services.sbling.net")
        + "---\n"
        + EXTERNAL_SECRET.format(store="bitwarden-secretsmanager")
    )
    rc, stderr = _run(manifest)
    assert rc == 1
    # both the bad host (rule + tls) and the bad store
    assert stderr.count("- ") >= 2


def test_empty_input_passes():
    rc, stderr = _run("")
    assert rc == 0
    assert stderr == ""


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
