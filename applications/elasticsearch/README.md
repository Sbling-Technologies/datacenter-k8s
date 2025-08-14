
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 868a85d10ed0218be46d1b9561261a61dee988d0
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```