
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout ed67d440963875f162af65f6e32d7108071c6f25
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```