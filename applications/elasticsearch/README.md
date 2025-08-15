
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 9c2fbc0164cc2d0bec03b73ecd2e9c9d2c0ee0a2
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```