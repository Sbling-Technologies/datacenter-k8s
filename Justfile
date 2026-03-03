_crds_schema_location := "https://raw.githubusercontent.com/datreeio/CRDs-catalog/main/{{.Group}}/{{.ResourceKind}}_{{.ResourceAPIVersion}}.json"
_k8s_schema_location := "https://raw.githubusercontent.com/yannh/kubernetes-json-schema/master/{{.NormalizedKubernetesVersion}}/{{.ResourceKind}}.json"

default:
    @just --list

kubeconform path:
    #!/usr/bin/env bash
    set -euo pipefail

    kustomize build --enable-helm "{{ path }}" | kubeconform \
    --strict \
    --schema-location default \
    --schema-location '{{ _crds_schema_location }}' \
    --schema-location '{{ _k8s_schema_location }}'

    echo "Validation successful for {{ path }}"

idempotent path:
    #!/usr/bin/env bash
    set -euo pipefail

    first_run=$(kustomize build --enable-helm "{{ path }}")
    second_run=$(kustomize build --enable-helm "{{ path }}")
    diff --unified=0 <(echo "$first_run") <(echo "$second_run")

    echo "Idempotency check passed for {{ path }}"
