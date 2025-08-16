# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 5218daf0ee55c07a0e9de60678c411fe85533d7a
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
