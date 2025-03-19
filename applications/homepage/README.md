# Homepage manifests

Documentation: [Homepage](https://gethomepage.dev/)

## Needed environment variable secrets

Set the following secrets in Hashicorp Vault under `homepage/env`:

- `HOMEPAGE_VAR_UNIFI_USER`, `HOMEPAGE_VAR_UNIFI_PSWD`: read-only access to UDM;
- `HOMEPAGE_VAR_PROXMOX_USER`, `HOMEPAGE_VAR_PROXMOX_PSWD`: read-only access to
  ProxmoxVE instance;
- `HOMEPAGE_VAR_GRAFANA_USER`, `HOMEPAGE_VAR_GRAFANA_PSWD`: read-only access to
  Grafana instance;
- `HOMEPAGE_VAR_TRUENAS_KEY`: read-only access to TrueNAS instance, api key;
