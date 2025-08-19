# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout e2bdf3da56266e564f173459d64314155ffc1cfd
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
