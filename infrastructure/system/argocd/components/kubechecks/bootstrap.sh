#!/usr/bin/env bash

set -euo pipefail

ARGOCD_USER="bootstrap-bot"
ARGOCD_PASS="$(cat /secrets/argocd-password)"

check_env() {
    required_env_vars=(
        "ARGOCD_PASS"
        "ARGOCD_SERVER"
        "ARGOCD_USER"
        "NAMESPACE"
        "SECRET_NAME"
    )
    for var in "${required_env_vars[@]}"; do
        if [ -z "${!var:-}" ]; then
            echo "Error: Environment variable '$var' is not set."
            exit 1
        fi
    done
}

check_if_secret_exists() {
    if kubectl -n "$NAMESPACE" get secret "$SECRET_NAME" >/dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

create_secret() {
    kubectl -n "$NAMESPACE" create secret generic "$SECRET_NAME" \
        --from-literal=token="$1"
}

argocd_login() {
    local -r session_token=$(
        curl -sk \
            -X POST "$ARGOCD_SERVER/api/v1/session" \
            -H "Content-Type: application/json" \
            -d "$(jq -n --arg user "$ARGOCD_USER" --arg pass "$ARGOCD_PASS" \
                '{username: $user, password: $pass}')" |
            jq -r '.token'
    )

    if [ -z "$session_token" ]; then
        echo "Failed to obtain Argo CD session token"
        exit 1
    fi

    echo "$session_token"
}

argocd_create_token() {
    local -r session_token="$1"
    local -r api_token=$(
        curl -sk \
            -X POST "$ARGOCD_SERVER/api/v1/account/other-app-user/token" \
            -H "Authorization: Bearer $session_token" \
            -H "Content-Type: application/json" \
            -d '{"name":"bootstrap","expiresIn":0}' |
            jq -r '.token'
    )

    if [ -z "$api_token" ]; then
        echo "Failed to create API token"
        exit 1
    fi

    echo "$api_token"
}

main() {
    check_env

    echo "Checking if token already exists..."
    if check_if_secret_exists; then
        echo "Token already exists in Kubernetes Secret '$SECRET_NAME'. Skipping bootstrap."
        exit 0
    fi

    echo "Logging into Argo CD..."
    local -r session_token=$(argocd_login)

    echo "Creating API token..."
    local -r api_token=$(argocd_create_token "$session_token")

    echo "Storing token as Kubernetes Secret..."
    create_secret "$api_token"

    echo "Bootstrap completed successfully"
}

main
