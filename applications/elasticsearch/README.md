
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 60688979c22bc90fc92997bfb8a2a6be32315ca0
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```