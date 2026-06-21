_crds_schema_location := "https://raw.githubusercontent.com/datreeio/CRDs-catalog/main/{{.Group}}/{{.ResourceKind}}_{{.ResourceAPIVersion}}.json"
_k8s_schema_location := "https://raw.githubusercontent.com/yannh/kubernetes-json-schema/master/{{.NormalizedKubernetesVersion}}/{{.ResourceKind}}.json"

default:
    @just --list

kubeconform path:
    #!/usr/bin/env bash
    set -euo pipefail

    for target in $(just _targets "{{ path }}"); do
        kustomize build --enable-helm "$target" | kubeconform \
        --strict \
        --schema-location default \
        --schema-location '{{ _crds_schema_location }}' \
        --schema-location '{{ _k8s_schema_location }}'
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
