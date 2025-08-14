
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout d1fa32ffaa20938fdd4f4e7d45e81ec6c9a8b709
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```