#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml", "pytest"]
# ///
"""Tests for hydrate_preview_hosts.py.

Run with:  uv run scripts/test_hydrate_preview_hosts.py
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

SCRIPT = Path(__file__).with_name("hydrate_preview_hosts.py")


def _load_module():
    spec = importlib.util.spec_from_file_location("hydrate_preview_hosts", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mod = _load_module()


# --- rewrite_host -----------------------------------------------------------


@pytest.mark.parametrize(
    "host,prefix,expected",
    [
        ("n8n.services.sbling.net", "preview-n8n-pr-42", "preview-n8n-pr-42.services.sbling.net"),
        ("webhooks.sbling.net", "preview-n8n-pr-42", "preview-n8n-pr-42.sbling.net"),
        ("games.dmz.sbling.net", "preview-pelican-pr-7", "preview-pelican-pr-7.dmz.sbling.net"),
        ("single", "preview-x-pr-1", "preview-x-pr-1"),
    ],
)
def test_rewrite_host_replaces_first_label(host, prefix, expected):
    assert mod.rewrite_host(host, prefix) == expected


# --- end-to-end via the CLI -------------------------------------------------

MANIFEST = """\
apiVersion: v1
kind: Namespace
metadata:
  name: preview-n8n-pr-42
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: n8n
  namespace: preview-n8n-pr-42
spec:
  rules:
    - host: n8n.services.sbling.net
      http:
        paths: []
  tls:
    - hosts:
        - n8n.services.sbling.net
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: n8n-webhooks
  namespace: preview-n8n-pr-42
spec:
  hostnames:
    - webhooks.sbling.net
  parentRefs:
    - name: external-gateway
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: n8n
  namespace: preview-n8n-pr-42
spec:
  template:
    spec:
      containers:
        - name: app
          image: n8n
"""


def _run(stdin: str, tmp_path: Path):
    urls_out = tmp_path / "urls.txt"
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--app", "n8n",
            "--pr", "42",
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
    urls = urls_out.read_text().split()
    return docs, urls


def test_ingress_hosts_rewritten(tmp_path):
    docs, _ = _run(MANIFEST, tmp_path)
    ingress = docs[("Ingress", "n8n")]
    assert ingress["spec"]["rules"][0]["host"] == "preview-n8n-pr-42.services.sbling.net"
    assert ingress["spec"]["tls"][0]["hosts"] == ["preview-n8n-pr-42.services.sbling.net"]


def test_httproute_hostnames_rewritten(tmp_path):
    docs, _ = _run(MANIFEST, tmp_path)
    route = docs[("HTTPRoute", "n8n-webhooks")]
    assert route["spec"]["hostnames"] == ["preview-n8n-pr-42.sbling.net"]


def test_namespace_and_other_resources_untouched(tmp_path):
    # Namespacing is kustomize's job; this script must not alter it.
    docs, _ = _run(MANIFEST, tmp_path)
    assert ("Namespace", "preview-n8n-pr-42") in docs
    deploy = docs[("Deployment", "n8n")]
    assert deploy["metadata"]["namespace"] == "preview-n8n-pr-42"
    assert deploy["spec"]["template"]["spec"]["containers"][0]["image"] == "n8n"


def test_urls_out_is_deduped_and_ordered(tmp_path):
    _, urls = _run(MANIFEST, tmp_path)
    # Ingress rule host first, then the HTTPRoute host; the TLS duplicate dropped.
    assert urls == [
        "preview-n8n-pr-42.services.sbling.net",
        "preview-n8n-pr-42.sbling.net",
    ]


def test_empty_input_is_safe(tmp_path):
    docs, urls = _run("", tmp_path)
    assert docs == {}
    assert urls == []


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
