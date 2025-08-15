
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout d14dc9ebe81e3089404a4a9fb6528b5962969fb2
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```