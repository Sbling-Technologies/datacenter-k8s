
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 5f324cddc57490d5d12dbf8c0c2fdcb0f18c83fb
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```