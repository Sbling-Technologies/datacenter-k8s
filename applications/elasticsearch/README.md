# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout ecb9345a342ada106c315b92dfe3afb15d979ca4
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
