
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 2daf4bd049628bacf65312ecb30e4988fa142cc5
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```