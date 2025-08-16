# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 340b1cfa19802a5b5f4fadf51f02d3ee28bbe257
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
