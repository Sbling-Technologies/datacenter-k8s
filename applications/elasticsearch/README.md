
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 58b8bb88a30e923c65ce8827869a86db69c57737
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```