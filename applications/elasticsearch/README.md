
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 7b85a66f91b7244c5f674b11e89adaff40039e62
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```