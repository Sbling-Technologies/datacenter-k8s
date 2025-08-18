# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 690f86c1403a97163b425170fa65a4414b900ddd
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
