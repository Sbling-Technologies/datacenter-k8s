
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 2855f245cc1cf9e3c0b3a9c57ad198e1d64fc822
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```