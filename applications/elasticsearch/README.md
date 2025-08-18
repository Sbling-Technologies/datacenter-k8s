# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 7d1a88bd1274c952f8a23e402923daace6be707a
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
