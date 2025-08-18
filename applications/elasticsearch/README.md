# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 7bc990eb70ae8bcbb3f5d2030ec470461e9e2128
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
