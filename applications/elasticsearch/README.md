
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 4ed336c446da1eb1a25686b06724004c28399756
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```