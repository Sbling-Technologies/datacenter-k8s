# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 37131db574104210933311862e00ba360ad19936
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
