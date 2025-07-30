
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 000f08a833ad76bdc2c9bbf535d6e6907f54e19f
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```