#!/usr/bin/env python3
# /// script
# dependencies = ["pyyaml"]
# ///
from typing import Any

from pathlib import Path
from pprint import pprint
import yaml

KUSTOMIZATION_FILENAME = "kustomization.yaml"


def list_files_in_folder(path: Path) -> set[str]:
    paths_to_check = set()

    directory_tree = path.walk()
    for directory, _, files in directory_tree:
        if "charts" in directory.parts:
            continue

        if KUSTOMIZATION_FILENAME in files and directory != path:
            continue

        filtered_files = filter(
            lambda f: f not in (KUSTOMIZATION_FILENAME, "values.yaml"), files
        )

        paths_to_check.update(
            map(lambda f: (directory / f).relative_to(path), filtered_files)
        )

    return paths_to_check


def _kustomize_from_generator(
    kustomization_yaml: dict[str, Any], generator_name: str
) -> list[str]:
    return sum(
        map(
            lambda cmg: cmg.get("files", []),
            kustomization_yaml.get(generator_name, []),
        ),
        [],
    )


def list_files_in_kustomization(path: Path) -> set[str]:
    kustomization_yaml = yaml.safe_load(path.read_text())

    k_resources = kustomization_yaml.get("resources", [])
    k_configmaps = _kustomize_from_generator(kustomization_yaml, "configMapGenerator")
    k_secrets = _kustomize_from_generator(kustomization_yaml, "secretGenerator")
    k_patches = list(
        filter(
            lambda p: p is not None,
            map(lambda p: p.get("path"), kustomization_yaml.get("patches", [])),
        )
    )

    k_all = k_resources + k_configmaps + k_secrets + k_patches
    k_without_urls = filter(lambda f: not f.startswith(("http://", "https://")), k_all)
    return set(map(lambda f: Path(f), k_without_urls))


def main() -> int:
    retval = 0

    repo = Path(".")
    kustomization_files = repo.glob("**/kustomization.yaml")

    for kf in kustomization_files:
        files_in_folder = list_files_in_folder(kf.parent)
        files_in_kustomization = list_files_in_kustomization(kf)

        missing_files = files_in_folder - files_in_kustomization
        if len(missing_files) > 0:
            print(f"Missing files in {kf}:")
            pprint(missing_files)
            retval = 1

    return retval


if __name__ == "__main__":
    raise SystemExit(main())
