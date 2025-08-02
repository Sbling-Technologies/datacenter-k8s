
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout d8e5b303b6330478b68202224eb69110983a6d3c
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```