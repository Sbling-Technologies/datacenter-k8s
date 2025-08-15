# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout d5f2d4d85fdf98fc842be65739498f5262318dcf
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
