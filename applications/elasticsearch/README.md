# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout b0b66aef30f28e35889506357ce9ee7bee93eab6
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
