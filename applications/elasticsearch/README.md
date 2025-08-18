# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 8ad17eb3f96488e7ceb552318dd7969bb24b338c
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
