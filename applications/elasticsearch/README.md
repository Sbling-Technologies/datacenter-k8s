# Manifest Hydration

To hydrate the manifests in this repository, run the following commands:

```shell
git clone git@github.com:Sbling-Technologies/datacenter-k8s.git
# cd into the cloned directory
git checkout e9a2457c085e2bbea1bfbd075bbec99b95fda727
kustomize build ./applications/elasticsearch/overlays/staging --enable-helm
```
