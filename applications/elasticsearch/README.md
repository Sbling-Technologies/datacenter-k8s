
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 517244730dca43ed7cc077c04b60c970080876cd
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```