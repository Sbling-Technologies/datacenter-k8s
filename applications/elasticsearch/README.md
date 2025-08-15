
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout a6163e3c91f2a835a4e5a3a8bbfdf3c96a1163f6
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```