
# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell

git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout eca543a30345a1331ea39483ff90d65ba72204e0
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```