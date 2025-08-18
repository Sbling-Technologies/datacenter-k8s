# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout cd1f5695310dec4be1d44c0353e4b8d985e991b5
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
