
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 8f037904ffe88cdbc87a092e92249ad21123000e
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```