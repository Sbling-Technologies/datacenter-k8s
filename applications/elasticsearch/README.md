# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout e367d348023493e0bde479909fbd8d8ad662b737
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
