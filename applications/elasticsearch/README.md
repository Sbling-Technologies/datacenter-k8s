
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout d5aa35944d4b694d50d5709ab2b99f010290e927
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```