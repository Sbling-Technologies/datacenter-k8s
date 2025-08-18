# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout e088f06ced661b962ddf748d0a89582e49ebf44e
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
