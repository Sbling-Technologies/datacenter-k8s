
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout 0f356fa24a68c6460adb80e0a5a2306369e251fe
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```