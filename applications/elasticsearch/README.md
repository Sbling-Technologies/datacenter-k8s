
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 890a3ee93f68c06d655612e2c0ac618d3a0e75fa
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```