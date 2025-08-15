
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 433c760bb893dce06b76a9c1eaf11328b595d023
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```