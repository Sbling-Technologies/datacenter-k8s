# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 2f60ff2a3d581395b9b9d29c0e07ff843ccc274d
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
