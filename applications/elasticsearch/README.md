
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout e9c9f0724c01f3067c5ecba3d0ee15e7b78d78bf
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```