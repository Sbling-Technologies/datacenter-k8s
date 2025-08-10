
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout c3d1cf19d50f7c8e63e53dd9f4f063a4c2fc6382
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```