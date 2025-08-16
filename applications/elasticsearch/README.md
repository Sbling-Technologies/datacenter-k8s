# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 7ae3eb9b907c467d9777924d2644c03a6086f163
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
