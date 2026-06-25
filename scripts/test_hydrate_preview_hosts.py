#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml", "pytest"]
# ///
"""Tests for hydrate_preview_hosts.py.

Run with:  uv run scripts/test_hydrate_preview_hosts.py
"""

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

SCRIPT = Path(__file__).with_name("hydrate_preview_hosts.py")
PLACEHOLDER = "<preview-url>"

MANIFEST = """\
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: n8n
spec:
  rules:
    - host: <preview-url>.services.sbling.net
  tls:
    - hosts:
        - <preview-url>.services.sbling.net
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: n8n-webhooks
spec:
  hostnames:
    - <preview-url>.sbling.net
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: n8n
  namespace: preview-n8n-pr-42
"""


def _run(stdin: str, tmp_path: Path):
    urls_out = tmp_path / "urls.txt"
    result = subprocess.run(
        [
            sys.executable, str(SCRIPT),
            "--app", "n8n",
            "--pr", "42",
            "--placeholder", PLACEHOLDER,
            "--urls-out", str(urls_out),
        ],
        input=stdin,
        capture_output=True,
        text=True,
        check=True,
    )
    docs = {
        (d["kind"], d["metadata"]["name"]): d
        for d in yaml.safe_load_all(result.stdout)
        if d
    }
    urls = urls_out.read_text().split() if urls_out.exists() else []
    return docs, urls


def test_placeholder_hosts_rewritten(tmp_path):
    docs, _ = _run(MANIFEST, tmp_path)
    ingress = docs[("Ingress", "n8n")]
    assert ingress["spec"]["rules"][0]["host"] == "preview-n8n-pr-42.services.sbling.net"
    assert ingress["spec"]["tls"][0]["hosts"] == ["preview-n8n-pr-42.services.sbling.net"]
    assert docs[("HTTPRoute", "n8n-webhooks")]["spec"]["hostnames"] == ["preview-n8n-pr-42.sbling.net"]


def test_non_host_resources_untouched(tmp_path):
    docs, _ = _run(MANIFEST, tmp_path)
    assert docs[("Deployment", "n8n")]["metadata"]["namespace"] == "preview-n8n-pr-42"


def test_urls_out_is_deduped_and_ordered(tmp_path):
    _, urls = _run(MANIFEST, tmp_path)
    assert urls == [
        "preview-n8n-pr-42.services.sbling.net",
        "preview-n8n-pr-42.sbling.net",
    ]


def test_non_placeholder_host_left_alone(tmp_path):
    manifest = """\
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: keep
spec:
  rules:
    - host: keep.services.sbling.net
"""
    docs, urls = _run(manifest, tmp_path)
    assert docs[("Ingress", "keep")]["spec"]["rules"][0]["host"] == "keep.services.sbling.net"
    assert urls == []


def test_empty_input_is_safe(tmp_path):
    docs, urls = _run("", tmp_path)
    assert docs == {}
    assert urls == []


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
