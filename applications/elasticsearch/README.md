
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout f54644fb1c32fecf1314e95847da81ad8d5bb79f
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```