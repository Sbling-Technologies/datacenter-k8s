# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 7505c95b4f73e77d4ab35c0426e31c00b8e3eb02
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
