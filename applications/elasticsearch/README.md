# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 94d9f6c74a1083a58eb7a4c62ff2eefc2d1f9d0c
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
