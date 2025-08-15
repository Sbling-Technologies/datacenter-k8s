
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout a98aefb5536fda545742dd2f636f6818dbb3a671
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```