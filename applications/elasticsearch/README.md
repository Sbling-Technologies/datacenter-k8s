
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout f65159087de3eae6708763fe594afbf3afe6f600
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```