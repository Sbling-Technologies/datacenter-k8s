
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 83a882c7ddb17b577f72a08e469b9ee1ebea2deb
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```