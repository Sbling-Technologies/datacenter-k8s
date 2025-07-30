
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 0f9d0cdce46a01452b22299dc7ad2b5353d610b3
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```