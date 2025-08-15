# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 989ae88bccd74800a940507f1e4b35697013e70b
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
