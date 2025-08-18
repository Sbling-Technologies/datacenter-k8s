# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 7ed3d0d0b07a00b06376afd07d4343d61a1763ad
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
