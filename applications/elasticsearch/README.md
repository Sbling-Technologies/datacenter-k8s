
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 1f927a16df6b303236433159e0df80b2e63b1510
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```