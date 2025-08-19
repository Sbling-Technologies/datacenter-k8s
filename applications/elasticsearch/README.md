# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 5d165a9893b89e6777fa117788fc6ff8885ab9f3
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
