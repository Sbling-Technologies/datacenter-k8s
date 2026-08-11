#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml"]
# ///
"""Rewrite preview placeholder hostnames in a hydrated manifest.

Reads a multi-document manifest (the output of `kustomize build`) from stdin,
replaces the --placeholder first DNS label of every Ingress/HTTPRoute hostname
with `preview-<app>-pr-<n>`, writes the result to stdout and the resulting public
URLs to --urls-out.

Assumes the manifest has already passed validate_preview.py.
"""

import argparse
import sys

import yaml


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app", required=True)
    parser.add_argument("--pr", required=True)
    parser.add_argument("--placeholder", required=True)
    parser.add_argument("--urls-out")
    args = parser.parse_args()

    prefix = f"preview-{args.app}-pr-{args.pr}"
    urls: list[str] = []

    def rewrite(host: str) -> str:
        labels = host.split(".")
        if labels[0] != args.placeholder:
            return host
        labels[0] = prefix
        new = ".".join(labels)
        urls.append(new)
        return new

    docs = []
    for doc in yaml.safe_load_all(sys.stdin):
        if not doc:
            continue
        kind = doc.get("kind")
        spec = doc.get("spec") or {}

        if kind == "Ingress":
            for rule in spec.get("rules") or []:
                if "host" in rule:
                    rule["host"] = rewrite(rule["host"])
            for tls in spec.get("tls") or []:
                if "hosts" in tls:
                    tls["hosts"] = [rewrite(h) for h in tls["hosts"]]

        elif kind == "HTTPRoute":
            if spec.get("hostnames"):
                spec["hostnames"] = [rewrite(h) for h in spec["hostnames"]]

        docs.append(doc)

    yaml.safe_dump_all(docs, sys.stdout, sort_keys=False)

    if args.urls_out:
        with open(args.urls_out, "w") as fh:
            for url in dict.fromkeys(urls):  # de-dup, preserve order
                fh.write(f"{url}\n")


if __name__ == "__main__":
    main()
