# Sbling Technologies Kubernetes HomeLab

This is the GitOps configuration of a shared HomeLab based on Kubernetes (using
ArgoCD) and maintained by:

- Lorenzo Bevilacqua: [LinkedIn](https://www.linkedin.com/in/lorenzo-bevilacqua),
  [GitHub](https://github.com/ardubev16).
- Luigi Miazzo: [LinkedIn](https://www.linkedin.com/in/luigi-miazzo), [GitHub](https://github.com/LuigiMiazzo17).

## Infrastructure Services

The Kubernetes cluster uses the following infrastructure services. These are reported
here as they shouldn't change much however, since the main focus of this HomeLab
is to learn new stuff, this list can get out of sync with respect to the actual implemented
services.

- **ArgoCD**: Deployed in a high-availability configuration for managing the GitOps
  workflow.
- **Cert-Manager**: For automated TLS certificate management, configured with both
  production and staging issuers.
- **Cilium**: A CNI plugin that provides advanced networking features, including
  network policies and service mesh capabilities. Currently also used as:
  - Kube-proxy replacement.
  - Ingress controller.
- **External DNS**: Manages DNS records dynamically based on Kubernetes resources.
- **Kured**: Kubernetes Reboot Daemon for automated node reboots after kernel updates.
- **Longhorn**: Provides distributed block storage for stateful applications.
- **MetalLB**: Handles load balancing for services in the bare-metal environment.
- **Monitoring**: A comprehensive monitoring and logging stack is deployed, including:
  - **Grafana**: for visualization and dashboards.
  - **Prometheus**: For metrics collection.
  - **Loki**: For log aggregation.
  - **Alloy**: For collecting and processing logs.
- **Traefik**: Serves as the ingress controller, with OIDC authentication integration.
- **CloudNativePG Operator**: Manages PostgreSQL databases within the cluster.
- **Keycloak Operator**: Manages Keycloak instances for identity and access management.

## Repository Structure

The structure of this repository represents what we think is a sensible organization
of manifests for a Kubernetes cluster. Here's a breakdown of the directory structure:

- `root-argocd-app.yaml`: The root ArgoCD application that bootstraps the entire
  cluster configuration. It points to the `appsets` directory.

- `appsets`: This directory contains ArgoCD ApplicationSets, which are responsible
  for deploying both infrastructure components and applications.

- `infrastructure`: This directory holds the Kubernetes manifests for the core infrastructure
  of the cluster. This includes operators, monitoring, logging, networking, and other
  system-level services. The manifests are organized by component and use Kustomize
  for configuration management.

- `applications`: Here you'll find the configurations for the various applications
  running in the cluster. Each application has its own directory, typically following
  a Kustomize structure with `base` and `overlays` for different environments.

- `misc`: This directory is for miscellaneous Kubernetes manifests and files that
  aren't deployed with ArgoCD.

- `apps`: _(Will be removed in favor of `applications` directory)_ This directory
  contains the ArgoCD Application definitions that are deployed by the `app-of-apps.yaml`.

- `vault`: _(Will be moved to `infrastructure` directory for consistency)_ This directory
  contains the configuration for HashiCorp Vault, which is used for secrets management.
