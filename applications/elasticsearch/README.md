
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 813ffbbfe7314874b0bae5dcc6f6f948af311d65
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```