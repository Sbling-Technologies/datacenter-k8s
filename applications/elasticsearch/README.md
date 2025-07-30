
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 913677a45ca97ef34d3d98a9fb7b4b65ade40e62
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```