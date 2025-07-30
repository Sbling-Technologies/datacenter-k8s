
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 4cf8a78c68c04f5a6f8c171c62be13ae97795517
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```