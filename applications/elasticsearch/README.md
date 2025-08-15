
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 877d9258efe95b5309c34f519932693b46f5dd71
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```