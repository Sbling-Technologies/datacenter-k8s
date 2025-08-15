# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout d971891914f2c691497525f7e7f66bd69ac76f70
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
