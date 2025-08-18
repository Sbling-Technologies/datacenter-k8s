# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout d5c71aaf89ff7965ec10d403b4b2130e89db6db0
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
