# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 40713f9cd075f131f1203f51a1d724b2343934d9
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
