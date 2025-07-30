
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout e955936b15186702ea4bceb7b80d61140b69a00d
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```