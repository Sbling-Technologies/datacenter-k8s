#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml"]
# ///
"""Validate that a hydrated preview manifest is safe to deploy.

Reads a multi-document manifest (the output of `kustomize build`) from stdin and
exits 1, listing the reasons on stderr, if either:
  * an ExternalSecret references the production secret store (--secret-store), or
  * an Ingress/HTTPRoute hostname does not use --placeholder as its first label.

The second rule proves the overlay parametrised the host for preview rather than
leaving the production hostname in place.
"""

import argparse
import sys

import yaml


def first_label(host: str) -> str:
    return host.split(".", 1)[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--secret-store", required=True)
    parser.add_argument("--placeholder", required=True)
    args = parser.parse_args()

    errors: list[str] = []

    for doc in yaml.safe_load_all(sys.stdin):
        if not doc:
            continue
        kind = doc.get("kind")
        name = (doc.get("metadata") or {}).get("name", "?")
        spec = doc.get("spec") or {}

        if kind == "ExternalSecret":
            store = (spec.get("secretStoreRef") or {}).get("name")
            if store == args.secret_store:
                errors.append(
                    f"ExternalSecret '{name}' references the production secret "
                    f"store '{args.secret_store}'"
                )

        elif kind == "Ingress":
            hosts = [rule["host"] for rule in spec.get("rules") or [] if "host" in rule]
            for tls in spec.get("tls") or []:
                hosts += tls.get("hosts") or []
            for host in hosts:
                if first_label(host) != args.placeholder:
                    errors.append(
                        f"Ingress '{name}' host '{host}' must use "
                        f"'{args.placeholder}' as its first label"
                    )

        elif kind == "HTTPRoute":
            for host in spec.get("hostnames") or []:
                if first_label(host) != args.placeholder:
                    errors.append(
                        f"HTTPRoute '{name}' hostname '{host}' must use "
                        f"'{args.placeholder}' as its first label"
                    )

    if errors:
        print("Preview validation failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
