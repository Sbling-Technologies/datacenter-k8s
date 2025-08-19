# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout cf78dda76a80136e11132a5768a257f10440a128
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
