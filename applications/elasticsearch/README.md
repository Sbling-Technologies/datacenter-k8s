# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout e6c1d57b9cdf78f194be52b13cf60fa31e2971c0
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
