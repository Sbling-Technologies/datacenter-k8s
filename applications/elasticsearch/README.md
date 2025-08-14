
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout e01d066850809ff0ded4b54096f80bef5302b78d
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```