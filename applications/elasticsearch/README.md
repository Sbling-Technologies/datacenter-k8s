
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 20b1ffc96961e8309b3576e0b41c94ee28c1e1c7
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```