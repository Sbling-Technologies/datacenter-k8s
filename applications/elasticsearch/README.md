
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 8960b85a4345c690b8da68090f8fe201befb6470
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```