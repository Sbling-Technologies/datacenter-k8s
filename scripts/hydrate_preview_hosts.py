#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml"]
# ///
"""Rewrite Ingress/HTTPRoute hostnames in a hydrated manifest for a PR preview.

Reads a multi-document Kubernetes manifest from stdin (the output of
`kustomize build`), replaces the leading DNS label of every exposed hostname
with `preview-<app>-pr-<n>` and writes the result to stdout. Namespaces are
handled by kustomize itself, not here.

The list of resulting public URLs is written, one per line, to the path given
by --urls-out (used to build the PR comment).
"""

import argparse
import sys

import yaml


def rewrite_host(host: str, prefix: str) -> str:
    """Replace the first DNS label, e.g. n8n.services.sbling.net -> <prefix>.services.sbling.net."""
    labels = host.split(".")
    labels[0] = prefix
    return ".".join(labels)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app", required=True)
    parser.add_argument("--pr", required=True)
    parser.add_argument("--urls-out")
    args = parser.parse_args()

    prefix = f"preview-{args.app}-pr-{args.pr}"
    urls: list[str] = []
    docs = []

    for doc in yaml.safe_load_all(sys.stdin):
        if not doc:
            continue
        kind = doc.get("kind")
        spec = doc.get("spec") or {}

        if kind == "Ingress":
            for rule in spec.get("rules") or []:
                if "host" in rule:
                    rule["host"] = rewrite_host(rule["host"], prefix)
                    urls.append(rule["host"])
            for tls in spec.get("tls") or []:
                if "hosts" in tls:
                    tls["hosts"] = [rewrite_host(h, prefix) for h in tls["hosts"]]

        elif kind == "HTTPRoute":
            hostnames = spec.get("hostnames") or []
            if hostnames:
                spec["hostnames"] = [rewrite_host(h, prefix) for h in hostnames]
                urls.extend(spec["hostnames"])

        docs.append(doc)

    yaml.safe_dump_all(docs, sys.stdout, sort_keys=False)

    if args.urls_out:
        with open(args.urls_out, "w") as fh:
            for url in dict.fromkeys(urls):  # de-dup, preserve order
                fh.write(f"{url}\n")


if __name__ == "__main__":
    main()
