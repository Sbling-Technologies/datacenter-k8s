
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 387bce33e9d7c3aad159bb01eb4ee43486eab4e8
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```