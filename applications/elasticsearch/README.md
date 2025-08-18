# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout fba6c8a75bd29885be82b3554000a319e679c08a
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
