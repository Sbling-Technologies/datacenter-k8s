# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 2e82e75bcba60b73f915b6d1e841ad89242f64a8
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
