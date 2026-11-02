# TODO

Issues to fix, found by a ponytail audit.

## Must fix

- [ ] **No off-cluster Postgres backups** (all CNPG `database.yaml`). Enable
      the barman-cloud `ObjectStore` with `plugins: [{name:
      barman-cloud.cloudnative-pg.io, isWALArchiver: true}]` per Cluster. Move
      wallabag from `longhorn-single-replica` (reclaim `Delete`) to
      `longhorn-single-replica-retain`.
- [ ] **n8n encryption key only on the PVC**
      (`applications/n8n/base/deployment.yaml`). Copy the key from
      `/home/node/.n8n/config` into Bitwarden and load it as
      `N8N_ENCRYPTION_KEY` via an ExternalSecret.

## Should fix

- [ ] **PR diff comment ignores `base/` changes**
      (`.github/workflows/show-application-diff.yaml`). Check out the whole app
      folder from master: `git checkout origin/master -- "${{ matrix.directory }}"`.
- [ ] **Pelican OIDC redirect mismatch** (`infrastructure/dex/config.yaml`).
      Dex lists `games.services.sbling.net`, the app runs on
      `games.dmz.sbling.net`. Change the redirect URI to
      `https://games.dmz.sbling.net/auth/oauth/callback/dex`.
- [ ] **Traefik dashboard serves the default certificate**
      (`infrastructure/traefik-system/values.yaml`). Add
      `ingressRoute.dashboard.tls.secretName: traefik-k8s-services-sbling-net-prod-cert`.
- [ ] **Traefik metric labels from client headers**
      (`infrastructure/traefik-system/values.yaml`). Delete `headerLabels`
      (unbounded Prometheus cardinality) and the copied example
      `metricRelabelings` / `relabelings`.
- [ ] **Postgres images never updated** (CNPG `imageName:`). Add a Renovate
      regex custom manager: `imageName: (?<depName>[^:\s]+):(?<currentValue>\S+)`
      with `datasourceTemplate: docker`.
- [ ] **Network policies copied in three places** (`argocd`, `n8n`,
      `unitn-tg-bot`). Move `default-deny-cross-namespace`,
      `allow-from-ingress` and `allow-monitoring` into one kustomize
      `Component` and include it from each.
- [ ] **Dex in-memory storage** (`infrastructure/dex/config.yaml`). Every Dex
      restart logs everyone out. Use
      `storage: {type: kubernetes, config: {inCluster: true}}`.
- [ ] **Dashboards from moving branches** (about 20 `GrafanaDashboard`
      objects). Pin GitHub URLs to the deployed tag and grafana.com URLs to a
      revision number.
- [ ] **Kafka on frozen `bitnamilegacy` image**
      (`applications/unitn-tg-bot/base/kafka/values.yaml`). Switch to
      `apache/kafka` (or Strimzi) so it gets patches.

## Nice to have

- [ ] **Delete dead config**: `cert-issuer-staging` (unused, shares the ACME
      account key secret with prod), `renso-ghcrio` pull secret (no pod uses
      it), the gatus `/config/dns.yaml` mount, Pelican's commented exporter,
      `exporter_config.yaml` and commented CNPG policy.
