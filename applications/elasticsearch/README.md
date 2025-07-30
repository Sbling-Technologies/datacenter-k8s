
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout d5a3a892c1fc45cc0c5bbbd6739bb5238f49cff2
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```