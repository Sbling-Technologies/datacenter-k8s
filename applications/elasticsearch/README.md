
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 9947378336e0991cd9c1ff1a7b26e28c0b2b61e8
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```