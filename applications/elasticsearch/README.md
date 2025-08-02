
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 592d18f55bb88f29e54c47036ce762df901ed52d
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```