# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 4f5d964c4dce0805478eaabbc86cba42bd465fb0
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
