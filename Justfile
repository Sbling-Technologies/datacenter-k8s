# CRDs-catalog has no releases: pin a commit of its main branch, so a broken catalog update fails the Renovate PR bumping it instead of every PR.
_crds_catalog_ref := "49729e49e8f062933e3716a26540d41b0cd0856c" # main
_crds_schema_location := "https://raw.githubusercontent.com/datreeio/CRDs-catalog/" + _crds_catalog_ref + "/{{.Group}}/{{.ResourceKind}}_{{.ResourceAPIVersion}}.json"
_k8s_schema_location := "https://raw.githubusercontent.com/yannh/kubernetes-json-schema/master/{{.NormalizedKubernetesVersion}}/{{.ResourceKind}}.json"
_local_schema_location := justfile_directory() + "/schemas/{{.Group}}/{{.ResourceKind}}_{{.ResourceAPIVersion}}.json"
_kubeconform := "kubeconform --strict --schema-location default --schema-location '" + _local_schema_location + "' --schema-location '" + _crds_schema_location + "' --schema-location '" + _k8s_schema_location + "'"

_openapi2jsonschema := "https://raw.githubusercontent.com/yannh/kubeconform/v0.8.0/scripts/openapi2jsonschema.py"

default:
    @just --list

kubeconform path:
    #!/usr/bin/env bash
    set -euo pipefail

    for target in $(just _targets "{{ path }}"); do
        kustomize build --enable-helm "$target" | {{ _kubeconform }}
    done

# Check that kubeconform can load the schema of every kind in the repository, without rendering anything.
# The stubs only carry a kind and a name, so they are expected to be invalid; a schema that is missing or fails to compile is reported as an error.
schemas-check:
    #!/usr/bin/env bash
    set -euo pipefail

    report=$(
        git ls-files -z 'applications/**.yaml' 'infrastructure/**.yaml' 'platform/**.yaml' ':!:**/kustomization.yaml' ':!:**/values.yaml' \
            | xargs -0 yq eval --no-doc 'select(tag == "!!map" and has("apiVersion") and has("kind")) | .apiVersion + " " + .kind' \
            | sort -u \
            | while read -r api_version kind; do
                printf -- '---\napiVersion: %s\nkind: %s\nmetadata:\n  name: schemas-check\n' "$api_version" "$kind"
            done \
            | {{ _kubeconform }} -output json
    ) || true  # kubeconform exits non-zero for the expected validation failures

    jq --exit-status 'has("resources")' <<< "$report" > /dev/null
    errors=$(jq --exit-status --raw-output '.resources[] | select(.status == "statusError") | "\(.version) \(.kind): \(.msg)"' <<< "$report") || [ $? -eq 4 ]
    if [ -n "$errors" ]; then
        echo "$errors"
        exit 1
    fi

# Regenerate ./schemas from every kro ResourceGraphDefinition. Needs access to a cluster: kro resolves the schemas of the templated resources through the API server.
kro-schemas:
    #!/usr/bin/env bash
    set -euo pipefail

    schemas_dir="{{ justfile_directory() }}/schemas"
    tmp=$(mktemp -d)
    trap 'rm -rf "$tmp"' EXIT

    rm -rf "$schemas_dir"
    grep -rlx --include='*.yaml' --exclude-dir=charts 'kind: ResourceGraphDefinition' "{{ justfile_directory() }}" | while read -r rgd; do
        group=$(yq '.spec.schema.group // "kro.run"' "$rgd")
        # The CLI leaves the CRD envelope and group to the controller; fill them in so openapi2jsonschema accepts it.
        kro generate crd --format json --file "$rgd" \
            | jq --arg group "$group" '.apiVersion = "apiextensions.k8s.io/v1" | .kind = "CustomResourceDefinition" | .spec.group = $group' \
            > "$tmp/crd.json"
        mkdir -p "$schemas_dir/$group"
        (cd "$schemas_dir/$group" && uv run --quiet --with pyyaml '{{ _openapi2jsonschema }}' "$tmp/crd.json")
    done

idempotent path:
    #!/usr/bin/env bash
    set -euo pipefail

    for target in $(just _targets "{{ path }}"); do
        first_run=$(kustomize build --enable-helm "$target")
        second_run=$(kustomize build --enable-helm "$target")
        diff --unified=0 <(echo "$first_run") <(echo "$second_run")
    done

# Applications are entered through envs/<env> overlays, so expand them to every env; other components are linted at the top level.
_targets path:
    #!/usr/bin/env bash
    set -euo pipefail

    if [ -d "{{ path }}/envs" ]; then
        for env_dir in "{{ path }}"/envs/*/; do
            echo "${env_dir%/}"
        done
    else
        echo "{{ path }}"
    fi

kref:
    ./scripts/check_kustomization_reference.py
