# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout f00dc8f85ee68b9a0f58c27ea92206d5947302d1
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
