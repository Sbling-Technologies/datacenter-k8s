# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 52cc9a70b05d13a38b984baa7efb501da8e30bb2
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
