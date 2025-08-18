# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout a3844fe5b12b02e32565b048c8a14f1bf6105715
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
