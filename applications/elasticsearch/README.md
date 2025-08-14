
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 3dcc25c78408a5e654f9648e2563a2f61082f199
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```