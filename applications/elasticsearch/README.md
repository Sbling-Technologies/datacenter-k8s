
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 8628f313a243d60b3687fe6857da98a6508ee4c4
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```