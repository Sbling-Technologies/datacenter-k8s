# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout d8cd7a621a5b2b0686d6a6f6e517ec6ac3608ecf
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
