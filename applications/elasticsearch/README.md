# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 86df994078c356b69da3f7cb5ff37777f35a5da1
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
