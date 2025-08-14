
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 28a20280d5fce89f7045a06eb4f209120e2c0faf
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```