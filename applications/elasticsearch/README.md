
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 4c3f8bd978cf0f56420e591bc326daa1a6cc92e2
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```