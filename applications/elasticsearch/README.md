# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 24c5a80cd6e6f3d6b7ba3841bbb29f8d82328d21
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
