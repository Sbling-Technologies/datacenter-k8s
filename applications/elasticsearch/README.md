
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 6773765067af7a8d949362276bd70d9b887fca52
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```