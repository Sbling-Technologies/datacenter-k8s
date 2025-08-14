
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout acec919abf9f467cd5efd2371880ff635a40a7f5
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```