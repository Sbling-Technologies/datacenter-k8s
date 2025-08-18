# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout bf5c3939b20b907bc068bc95a827da1bce1f291a
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
