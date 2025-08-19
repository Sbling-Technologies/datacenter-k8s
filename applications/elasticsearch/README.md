# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 07b4ec282a225e1465b3b1ec1b14b36c9c1eca68
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
