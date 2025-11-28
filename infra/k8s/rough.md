
docker build -t prsh17/posts:0.0.1 . [to build image]
docker push prsh17/posts [to push img to dockre hub] 

kubectl apply -f posts.yaml [to build pod]
kubectl apply -f .
kubectl get pods
kubectl logs posts
kubectl delete pod posts
kubectl describe pod posts [to get some more info abt pod]
kubectl exec -it posts -- sh [to get into shell of pod/container]

kubectl apply -f . [apply all files]
kubectl apply -f posts-depl.yaml [to build deployment]
kubectl get deployments
kubectl describe deployment posts-depl
kubectl logs posts-depl-666f9cdcc7-b6l5f
kubectl rollout restart deployment posts-depl
kubectl delete deployment posts-depl

kubectl get services
kubectl describe service port-srv

skaffold dev
skaffold run
skaffold delete

access on products.com

kubectl -n kubernetes-dashboard create token admin-user
kubectl -n kubernetes-dashboard create serviceaccount admin-user
kubectl create clusterrolebinding admin-user --clusterrole=cluster-admin --serviceaccount=kubernetes-dashboard:admin-user


kubectl -n kubernetes-dashboard create token admin-user


TO view dashboard:
kubectl proxy
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/


purva@purva-devops:~$ sudo iptables -nvL
[sudo] password for purva: 
sudo: a password is required
purva@purva-devops:~$ ^C
purva@purva-devops:~$ cd /home/purva/work/k8s-launch-pad/infra/k8s
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl apply client-depl.yml 
error: Unexpected args: [client-depl.yml]
See 'kubectl apply -h' for help and examples
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl apply -h
Apply a configuration to a resource by file name or stdin. The resource name must be specified. This resource will be
created if it doesn't exist yet. To use 'apply', always create the resource initially with either 'apply' or 'create
--save-config'.

 JSON and YAML formats are accepted.

 Alpha Disclaimer: the --prune functionality is not yet complete. Do not use unless you are aware of what the current
state is. See https://issues.k8s.io/34274.

Examples:
  # Apply the configuration in pod.json to a pod
  kubectl apply -f ./pod.json
  
  # Apply resources from a directory containing kustomization.yaml - e.g. dir/kustomization.yaml
  kubectl apply -k dir/
  
  # Apply the JSON passed into stdin to a pod
  cat pod.json | kubectl apply -f -
  
  # Apply the configuration from all files that end with '.json'
  kubectl apply -f '*.json'
  
  # Note: --prune is still in Alpha
  # Apply the configuration in manifest.yaml that matches label app=nginx and delete all other resources that are not in
the file and match label app=nginx
  kubectl apply --prune -f manifest.yaml -l app=nginx
  
  # Apply the configuration in manifest.yaml and delete all the other config maps that are not in the file
  kubectl apply --prune -f manifest.yaml --all --prune-allowlist=core/v1/ConfigMap

Available Commands:
  edit-last-applied   Edit latest last-applied-configuration annotations of a resource/object
  set-last-applied    Set the last-applied-configuration annotation on a live object to match the contents of a file
  view-last-applied   View the latest last-applied-configuration annotations of a resource/object

Options:
    --all=false:
	Select all resources in the namespace of the specified resource types.

    --allow-missing-template-keys=true:
	If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to
	golang and jsonpath output formats.

    --cascade='background':
	Must be "background", "orphan", or "foreground". Selects the deletion cascading strategy for the dependents
	(e.g. Pods created by a ReplicationController). Defaults to background.

    --dry-run='none':
	Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without
	sending it. If server strategy, submit server-side request without persisting the resource.

    --field-manager='kubectl-client-side-apply':
	Name of the manager used to track field ownership.

    -f, --filename=[]:
	The files that contain the configurations to apply.

    --force=false:
	If true, immediately remove resources from API and bypass graceful deletion. Note that immediate deletion of
	some resources may result in inconsistency or data loss and requires confirmation.

    --force-conflicts=false:
	If true, server-side apply will force the changes against conflicts.

    --grace-period=-1:
	Period of time in seconds given to the resource to terminate gracefully. Ignored if negative. Set to 1 for
	immediate shutdown. Can only be set to 0 when --force is true (force deletion).

    -k, --kustomize='':
	Process a kustomization directory. This flag can't be used together with -f or -R.

    --openapi-patch=true:
	If true, use openapi to calculate diff when the openapi presents and the resource can be found in the openapi
	spec. Otherwise, fall back to use baked-in types.

    -o, --output='':
	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile, jsonpath,
	jsonpath-as-json, jsonpath-file).

    --overwrite=true:
	Automatically resolve conflicts between the modified and live configuration by using values from the modified
	configuration

    --prune=false:
	Automatically delete resource objects, that do not appear in the configs and are created by either apply or
	create --save-config. Should be used with either -l or --all.

    --prune-allowlist=[]:
	Overwrite the default allowlist with <group/version/kind> for --prune

    -R, --recursive=false:
	Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests
	organized within the same directory.

    -l, --selector='':
	Selector (label query) to filter on, supports '=', '==', '!=', 'in', 'notin'.(e.g. -l
	key1=value1,key2=value2,key3 in (value3)). Matching objects must satisfy all of the specified label
	constraints.

    --server-side=false:
	If true, apply runs in the server instead of the client.

    --show-managed-fields=false:
	If true, keep the managedFields when printing objects in JSON or YAML format.

    --subresource='':
	If specified, apply will operate on the subresource of the requested object.  Only allowed when using
	--server-side.

    --template='':
	Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format
	is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

    --timeout=0s:
	The length of time to wait before giving up on a delete, zero means determine a timeout from the size of the
	object

    --validate='strict':
	Must be one of: strict (or true), warn, ignore (or false). "true" or "strict" will use a schema to validate
	the input and fail the request if invalid. It will perform server side validation if ServerSideFieldValidation
	is enabled on the api-server, but will fall back to less reliable client-side validation if not. "warn" will
	warn about unknown or duplicate fields without blocking the request if server-side field validation is enabled
	on the API server, and behave as "ignore" otherwise. "false" or "ignore" will not perform any schema
	validation, silently dropping any unknown or duplicate fields.

    --wait=false:
	If true, wait for resources to be gone before returning. This waits for finalizers.

Usage:
  kubectl apply (-f FILENAME | -k DIRECTORY) [options]

Use "kubectl apply <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl apply -f client-depl.yml 
deployment.apps/my-python-app created
service/my-python-app created
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl get pods
NAME                             READY   STATUS         RESTARTS   AGE
my-python-app-79684bfc76-zbjwr   0/1     ErrImagePull   0          13s
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl apply -f client-depl.yml 
error: error parsing client-depl.yml: error converting YAML to JSON: yaml: line 17: mapping values are not allowed in this context
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl apply -f client-depl.yml 
deployment.apps/my-python-app unchanged
service/my-python-app unchanged
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
my-python-app-79684bfc76-zbjwr   1/1     Running   0          6m19s
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl apply -f client-depl.yml 
deployment.apps/my-python-app configured
service/my-python-app configured
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl get pods
NAME                             READY   STATUS              RESTARTS   AGE
my-python-app-5bb45c7b64-k6tnw   0/1     ContainerCreating   0          2s
my-python-app-79684bfc76-zbjwr   1/1     Running             0          8m13s
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl describe deployment 
Name:                   my-python-app
Namespace:              default
CreationTimestamp:      Thu, 27 Nov 2025 20:13:14 +0530
Labels:                 <none>
Annotations:            deployment.kubernetes.io/revision: 2
Selector:               app=my-python-app
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=my-python-app
  Containers:
   my-python-app:
    Image:      ghcr.io/prsh17/my-python-app:v1.0.0
    Port:       8000/TCP
    Host Port:  0/TCP
    Environment:
      PORT:        8000
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  my-python-app-79684bfc76 (0/0 replicas created)
NewReplicaSet:   my-python-app-5bb45c7b64 (1/1 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  8m33s  deployment-controller  Scaled up replica set my-python-app-79684bfc76 to 1
  Normal  ScalingReplicaSet  22s    deployment-controller  Scaled up replica set my-python-app-5bb45c7b64 to 1
  Normal  ScalingReplicaSet  20s    deployment-controller  Scaled down replica set my-python-app-79684bfc76 to 0 from 1
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl delete deployment my-python-app-5bb45c7b64-k6tnw
Error from server (NotFound): deployments.apps "my-python-app-5bb45c7b64-k6tnw" not found
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl describe deployment 
Name:                   my-python-app
Namespace:              default
CreationTimestamp:      Thu, 27 Nov 2025 20:13:14 +0530
Labels:                 <none>
Annotations:            deployment.kubernetes.io/revision: 2
Selector:               app=my-python-app
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=my-python-app
  Containers:
   my-python-app:
    Image:      ghcr.io/prsh17/my-python-app:v1.0.0
    Port:       8000/TCP
    Host Port:  0/TCP
    Environment:
      PORT:        8000
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  my-python-app-79684bfc76 (0/0 replicas created)
NewReplicaSet:   my-python-app-5bb45c7b64 (1/1 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  9m25s  deployment-controller  Scaled up replica set my-python-app-79684bfc76 to 1
  Normal  ScalingReplicaSet  74s    deployment-controller  Scaled up replica set my-python-app-5bb45c7b64 to 1
  Normal  ScalingReplicaSet  72s    deployment-controller  Scaled down replica set my-python-app-79684bfc76 to 0 from 1
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
my-python-app-5bb45c7b64-k6tnw   1/1     Running   0          78s
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl describe deployment 
Name:                   my-python-app
Namespace:              default
CreationTimestamp:      Thu, 27 Nov 2025 20:13:14 +0530
Labels:                 <none>
Annotations:            deployment.kubernetes.io/revision: 2
Selector:               app=my-python-app
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=my-python-app
  Containers:
   my-python-app:
    Image:      ghcr.io/prsh17/my-python-app:v1.0.0
    Port:       8000/TCP
    Host Port:  0/TCP
    Environment:
      PORT:        8000
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  my-python-app-79684bfc76 (0/0 replicas created)
NewReplicaSet:   my-python-app-5bb45c7b64 (1/1 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  9m39s  deployment-controller  Scaled up replica set my-python-app-79684bfc76 to 1
  Normal  ScalingReplicaSet  88s    deployment-controller  Scaled up replica set my-python-app-5bb45c7b64 to 1
  Normal  ScalingReplicaSet  86s    deployment-controller  Scaled down replica set my-python-app-79684bfc76 to 0 from 1
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl describe deployment kubectl logs deployment/my
error: there is no need to specify a resource type as a separate argument when passing arguments in resource/name form (e.g. 'kubectl get resource/<resource_name>' instead of 'kubectl get resource resource/<resource_name>'
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl describe deployment kubectl logs deployment/my-python-app-5bb45c7b64-k6tnw
error: there is no need to specify a resource type as a separate argument when passing arguments in resource/name form (e.g. 'kubectl get resource/<resource_name>' instead of 'kubectl get resource resource/<resource_name>'
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl apply -f client-depl.yml 
deployment.apps/my-python-app unchanged
service/my-python-app configured
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl describe deployment kubectl logs deployment
Error from server (NotFound): deployments.apps "kubectl" not found
Error from server (NotFound): deployments.apps "logs" not found
Error from server (NotFound): deployments.apps "deployment" not found
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ 
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl logs deployment
error: error from server (NotFound): pods "deployment" not found in namespace "default"
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl describe deployment
Name:                   my-python-app
Namespace:              default
CreationTimestamp:      Thu, 27 Nov 2025 20:13:14 +0530
Labels:                 <none>
Annotations:            deployment.kubernetes.io/revision: 2
Selector:               app=my-python-app
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=my-python-app
  Containers:
   my-python-app:
    Image:      ghcr.io/prsh17/my-python-app:v1.0.0
    Port:       8000/TCP
    Host Port:  0/TCP
    Environment:
      PORT:        8000
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  my-python-app-79684bfc76 (0/0 replicas created)
NewReplicaSet:   my-python-app-5bb45c7b64 (1/1 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  13m    deployment-controller  Scaled up replica set my-python-app-79684bfc76 to 1
  Normal  ScalingReplicaSet  5m32s  deployment-controller  Scaled up replica set my-python-app-5bb45c7b64 to 1
  Normal  ScalingReplicaSet  5m30s  deployment-controller  Scaled down replica set my-python-app-79684bfc76 to 0 from 1
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl get nodes
NAME                 STATUS   ROLES           AGE   VERSION
kind-control-plane   Ready    control-plane   23m   v1.27.3
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl get pos
error: the server doesn't have a resource type "pos"
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
my-python-app-5bb45c7b64-k6tnw   1/1     Running   0          6m1s
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl get nodes -o wide
NAME                 STATUS   ROLES           AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE                         KERNEL-VERSION      CONTAINER-RUNTIME
kind-control-plane   Ready    control-plane   23m   v1.27.3   172.19.0.2    <none>        Debian GNU/Linux 11 (bullseye)   6.14.0-33-generic   containerd://1.7.1
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ curl http://localhost:30080/
curl: (7) Failed to connect to localhost port 30080 after 3 ms: Couldn't connect to server
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl apply -f .
deployment.apps/my-python-app unchanged
service/my-python-app unchanged
deployment.apps/nginx-api-deployment created
The Service "nginx-api-service" is invalid: spec.ports[0].nodePort: Invalid value: 30080: provided port is already allocated
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl apply -f nginx-depl.yml 
deployment.apps/nginx-api-deployment configured
The Service "nginx-api-service" is invalid: spec.ports[0].nodePort: Invalid value: 30080: provided port is already allocated
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl apply -f nginx-depl.yml 
deployment.apps/nginx-api-deployment unchanged
service/nginx-api-service created
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp4s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 84:a9:38:d7:2d:94 brd ff:ff:ff:ff:ff:ff
3: wlp0s20f3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 1c:c1:0c:f8:83:ab brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.141/24 brd 192.168.1.255 scope global dynamic noprefixroute wlp0s20f3
       valid_lft 582737sec preferred_lft 582737sec
4: br-9d84ea2322d8: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 6e:68:43:49:71:b7 brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-9d84ea2322d8
       valid_lft forever preferred_lft forever
5: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether e2:1c:2b:92:5f:d7 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
6: veth1b78e1c@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default 
    link/ether a2:91:e1:04:7a:60 brd ff:ff:ff:ff:ff:ff link-netnsid 0
21: vboxnet0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 0a:00:27:00:00:00 brd ff:ff:ff:ff:ff:ff
22: vboxnet1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 0a:00:27:00:00:01 brd ff:ff:ff:ff:ff:ff
    inet 192.168.59.1/24 brd 192.168.59.255 scope global vboxnet1
       valid_lft forever preferred_lft forever
39: br-8bc964c03dae: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default 
    link/ether ca:d1:96:9f:19:c1 brd ff:ff:ff:ff:ff:ff
    inet 172.19.0.1/16 brd 172.19.255.255 scope global br-8bc964c03dae
       valid_lft forever preferred_lft forever
40: br-139061edc18a: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether da:ed:cd:b0:0e:72 brd ff:ff:ff:ff:ff:ff
    inet 172.19.0.1/16 brd 172.19.255.255 scope global br-139061edc18a
       valid_lft forever preferred_lft forever
41: veth933970c@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-139061edc18a state UP group default 
    link/ether 42:4d:6b:2c:86:5a brd ff:ff:ff:ff:ff:ff link-netnsid 1
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl get nodes -o wide
NAME                 STATUS   ROLES           AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE                         KERNEL-VERSION      CONTAINER-RUNTIME
kind-control-plane   Ready    control-plane   47m   v1.27.3   172.19.0.2    <none>        Debian GNU/Linux 11 (bullseye)   6.14.0-33-generic   containerd://1.7.1
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ sudo iptables -nvL
[sudo] password for purva: 
Chain INPUT (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:2707
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:1515
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:1514
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:1515
 586K  162M ACCEPT     0    --  lo     *       0.0.0.0/0            0.0.0.0/0           
    0     0 LOG        6    --  !lo    *       0.0.0.0/0            127.0.0.0/8          LOG flags 0 level 4 prefix "iptables_IN_lo DROP 0 "
    0     0 DROP       6    --  !lo    *       0.0.0.0/0            127.0.0.0/8         
6445K 6672M ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            state ESTABLISHED
70023   13M ACCEPT     17   --  *      *       0.0.0.0/0            0.0.0.0/0            state ESTABLISHED
    0     0 ACCEPT     1    --  *      *       0.0.0.0/0            0.0.0.0/0            state ESTABLISHED
    0     0 ACCEPT     0    --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
    4   184 DROP       0    --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate INVALID
 5004  832K DROP       0    --  *      *       0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type BROADCAST
 5246  975K DROP       0    --  *      *       0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type MULTICAST
    0     0 DROP       0    --  *      *       0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type ANYCAST
    0     0 DROP       0    --  *      *       0.0.0.0/0            224.0.0.0/4         
    6  1316 LOG        0    --  *      *       0.0.0.0/0            0.0.0.0/0            LOG flags 0 level 4 prefix "IPT_INP"
    0     0 REJECT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:113 flags:0x17/0x02 ctstate NEW reject-with tcp-reset
    6  1316 LOG        0    --  *      *       0.0.0.0/0            0.0.0.0/0            limit: avg 1/sec burst 100 LOG flags 0 level 4 prefix "iptables[DOS]: "
    0     0 ACCEPT     17   --  *      *       0.0.0.0/0            0.0.0.0/0            udp spt:123
    6  1316 DROP       0    --  *      *       0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:1514
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp spt:1515
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:1510

Chain FORWARD (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
92950  106M DOCKER-USER  0    --  *      *       0.0.0.0/0            0.0.0.0/0           
92950  106M DOCKER-FORWARD  0    --  *      *       0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     0    --  *      br-022fab32946d  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
    0     0 DOCKER     0    --  *      br-022fab32946d  0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     0    --  br-022fab32946d !br-022fab32946d  0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     0    --  br-022fab32946d br-022fab32946d  0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     0    --  *      br-237601346bf4  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
    0     0 DOCKER     0    --  *      br-237601346bf4  0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     0    --  br-237601346bf4 !br-237601346bf4  0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     0    --  br-237601346bf4 br-237601346bf4  0.0.0.0/0            0.0.0.0/0           
    0     0 LOG        0    --  *      *       0.0.0.0/0            0.0.0.0/0            LOG flags 0 level 4 prefix "IPT_FWD "

Chain OUTPUT (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
 586K  162M ACCEPT     0    --  *      lo      0.0.0.0/0            0.0.0.0/0           
2893K 1386M ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            state ESTABLISHED
   60  5234 ACCEPT     17   --  *      *       0.0.0.0/0            0.0.0.0/0            state ESTABLISHED
    0     0 ACCEPT     1    --  *      *       0.0.0.0/0            0.0.0.0/0            state NEW,ESTABLISHED
 113K   15M LOG        0    --  *      *       0.0.0.0/0            0.0.0.0/0            LOG flags 0 level 4 prefix "IPT_OUT"
  126  9576 ACCEPT     17   --  *      *       0.0.0.0/0            0.0.0.0/0            udp dpt:123
    0     0 ACCEPT     17   --  *      *       0.0.0.0/0            0.0.0.0/0            udp dpts:33434:33523 state NEW
 4744 6063K ACCEPT     17   --  *      *       0.0.0.0/0            0.0.0.0/0            multiport dports 19302:19309,443
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            104.192.136.0/21     tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            185.166.140.0/22     tcp dpt:22
   36  2160 ACCEPT     6    --  *      *       0.0.0.0/0            13.200.41.128/25     tcp dpt:22
69988 6067K ACCEPT     17   --  *      *       0.0.0.0/0            0.0.0.0/0            udp dpt:53
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:53
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:25
    4   240 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:587
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp spt:80
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp spt:443
  550 32936 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:80
32931 1974K ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:443
   33  1972 ACCEPT     6    --  *      *       0.0.0.0/0            172.0.0.0/8          tcp
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:2707
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:1510
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            192.168.56.5         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            192.168.56.6         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            192.168.56.5         tcp dpt:4565
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            192.168.56.6         tcp dpt:4565
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            16.171.255.8         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            192.168.56.7         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            192.168.56.2         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.3.235         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.0.94          tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            65.2.187.197         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.2.226         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            65.2.187.197         tcp dpt:7045
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.3.173         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.3.68          tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.2.227         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.2.14          tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            13.233.197.110       tcp dpt:4930
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            43.204.164.168       tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            43.204.164.168       tcp dpt:7045
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            43.204.164.168       tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.3.102         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.3.142         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            43.204.164.168       tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            43.204.164.168       tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            3.110.14.8           tcp dpt:5748
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            3.110.14.8           tcp dpt:5784
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            35.154.175.91        tcp dpt:10623
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            13.232.34.210        tcp dpt:6066
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            15.206.73.249        tcp dpt:5678
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            10.0.0.150           tcp dpt:7529
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            3.108.40.155         tcp dpt:10623
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            10.0.7.20            tcp dpt:10623
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.40.0.176         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.40.0.242         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            3.111.217.57         tcp dpt:4930
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.40.0.242         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            43.205.228.14        tcp dpt:4930
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            13.232.130.198       tcp dpt:4930
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            3.109.103.145        tcp dpt:7448
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            18.16.174.177        tcp dpt:7448
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            18.16.174.177        tcp dpt:7448
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            18.16.174.177        tcp dpt:7448
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            18.61.174.177        tcp dpt:7448
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            10.112.0.149         tcp dpt:7448
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            35.154.175.91        tcp dpt:10623
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            52.66.186.67         tcp dpt:6547
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            13.232.34.210        tcp dpt:6066
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            43.204.35.161        tcp dpt:6534
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            13.234.116.175       tcp dpt:2983
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            13.235.99.50         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            13.235.99.50         tcp dpt:6066
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            13.201.120.236       tcp dpt:6066
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            52.66.211.163        tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            13.233.123.147       tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            65.2.146.115         tcp dpt:22
  269 16140 ACCEPT     6    --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:23123
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            52.66.197.81         tcp dpt:9185
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            65.2.146.115         tcp dpt:6066
    6   360 ACCEPT     6    --  *      *       0.0.0.0/0            65.0.101.42          tcp dpt:2504
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            65.0.101.42          tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            10.50.36.95          tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            10.50.36.95          tcp dpt:2504
 4620  612K DROP       0    --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain DOCKER (5 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 ACCEPT     6    --  !br-139061edc18a br-139061edc18a  0.0.0.0/0            172.19.0.2           tcp dpt:6443
    0     0 DROP       0    --  !br-9d84ea2322d8 br-9d84ea2322d8  0.0.0.0/0            0.0.0.0/0           
    0     0 DROP       0    --  !docker0 docker0  0.0.0.0/0            0.0.0.0/0           
    0     0 DROP       0    --  !br-139061edc18a br-139061edc18a  0.0.0.0/0            0.0.0.0/0           

Chain DOCKER-BRIDGE (1 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 DOCKER     0    --  *      br-9d84ea2322d8  0.0.0.0/0            0.0.0.0/0           
    0     0 DOCKER     0    --  *      docker0  0.0.0.0/0            0.0.0.0/0           
    0     0 DOCKER     0    --  *      br-139061edc18a  0.0.0.0/0            0.0.0.0/0           

Chain DOCKER-CT (1 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 ACCEPT     0    --  *      br-9d84ea2322d8  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
 8031   12M ACCEPT     0    --  *      docker0  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
62697   93M ACCEPT     0    --  *      br-139061edc18a  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED

Chain DOCKER-FORWARD (1 references)
 pkts bytes target     prot opt in     out     source               destination         
92950  106M DOCKER-CT  0    --  *      *       0.0.0.0/0            0.0.0.0/0           
22222 1317K DOCKER-ISOLATION-STAGE-1  0    --  *      *       0.0.0.0/0            0.0.0.0/0           
22222 1317K DOCKER-BRIDGE  0    --  *      *       0.0.0.0/0            0.0.0.0/0           
    0     0 ACCEPT     0    --  br-9d84ea2322d8 *       0.0.0.0/0            0.0.0.0/0           
 2631  188K ACCEPT     0    --  docker0 *       0.0.0.0/0            0.0.0.0/0           
19591 1129K ACCEPT     0    --  br-139061edc18a *       0.0.0.0/0            0.0.0.0/0           

Chain DOCKER-ISOLATION-STAGE-1 (1 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 DOCKER-ISOLATION-STAGE-2  0    --  br-9d84ea2322d8 !br-9d84ea2322d8  0.0.0.0/0            0.0.0.0/0           
 2631  188K DOCKER-ISOLATION-STAGE-2  0    --  docker0 !docker0  0.0.0.0/0            0.0.0.0/0           
19591 1129K DOCKER-ISOLATION-STAGE-2  0    --  br-139061edc18a !br-139061edc18a  0.0.0.0/0            0.0.0.0/0           

Chain DOCKER-ISOLATION-STAGE-2 (3 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 DROP       0    --  *      br-139061edc18a  0.0.0.0/0            0.0.0.0/0           
    0     0 DROP       0    --  *      docker0  0.0.0.0/0            0.0.0.0/0           
    0     0 DROP       0    --  *      br-9d84ea2322d8  0.0.0.0/0            0.0.0.0/0           

Chain DOCKER-USER (1 references)
 pkts bytes target     prot opt in     out     source               destination         
92950  106M RETURN     0    --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain ICMPFLOOD (0 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0            0    --  *      *       0.0.0.0/0            0.0.0.0/0            recent: SET name: ICMP side: source mask: 255.255.255.255
    0     0 LOG        0    --  *      *       0.0.0.0/0            0.0.0.0/0            recent: UPDATE seconds: 1 hit_count: 6 TTL-Match name: ICMP side: source mask: 255.255.255.255 limit: avg 1/sec burst 1 LOG flags 0 level 4 prefix "iptables[ICMP-flood]: "
    0     0 DROP       0    --  *      *       0.0.0.0/0            0.0.0.0/0            recent: UPDATE seconds: 1 hit_count: 6 TTL-Match name: ICMP side: source mask: 255.255.255.255
    0     0 ACCEPT     0    --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain SSHBRUTE (0 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0            0    --  *      *       0.0.0.0/0            0.0.0.0/0            recent: SET name: SSH side: source mask: 255.255.255.255
    0     0 LOG        0    --  *      *       0.0.0.0/0            0.0.0.0/0            recent: UPDATE seconds: 300 hit_count: 10 name: SSH side: source mask: 255.255.255.255 limit: avg 1/sec burst 100 LOG flags 0 level 4 prefix "iptables[SSH-brute]: "
    0     0 DROP       0    --  *      *       0.0.0.0/0            0.0.0.0/0            recent: UPDATE seconds: 300 hit_count: 10 name: SSH side: source mask: 255.255.255.255
    0     0 ACCEPT     0    --  *      *       0.0.0.0/0            0.0.0.0/0           
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ sudo iptables -nvL | grep 172
   33  1972 ACCEPT     6    --  *      *       0.0.0.0/0            172.0.0.0/8          tcp
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.3.235         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.0.94          tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.2.226         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.3.173         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.3.68          tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.2.227         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.2.14          tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.3.102         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.41.3.142         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.40.0.176         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.40.0.242         tcp dpt:22
    0     0 ACCEPT     6    --  *      *       0.0.0.0/0            172.40.0.242         tcp dpt:22
    0     0 ACCEPT     6    --  !br-139061edc18a br-139061edc18a  0.0.0.0/0            172.19.0.2           tcp dpt:6443
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl get pods
NAME                                    READY   STATUS    RESTARTS   AGE
my-python-app-5bb45c7b64-k6tnw          1/1     Running   0          36m
nginx-api-deployment-746876665c-ttqvc   1/1     Running   0          16m
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl exec -it nginx-api-deployment-746876665c-ttqvc
error: you must specify at least one command for the container
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl exec --help
Execute a command in a container.

Examples:
  # Get output from running the 'date' command from pod mypod, using the first container by default
  kubectl exec mypod -- date
  
  # Get output from running the 'date' command in ruby-container from pod mypod
  kubectl exec mypod -c ruby-container -- date
  
  # Switch to raw terminal mode; sends stdin to 'bash' in ruby-container from pod mypod
  # and sends stdout/stderr from 'bash' back to the client
  kubectl exec mypod -c ruby-container -i -t -- bash -il
  
  # List contents of /usr from the first container of pod mypod and sort by modification time
  # If the command you want to execute in the pod has any flags in common (e.g. -i),
  # you must use two dashes (--) to separate your command's flags/arguments
  # Also note, do not surround your command and its flags/arguments with quotes
  # unless that is how you would execute it normally (i.e., do ls -t /usr, not "ls -t /usr")
  kubectl exec mypod -i -t -- ls -t /usr
  
  # Get output from running 'date' command from the first pod of the deployment mydeployment, using the first container
by default
  kubectl exec deploy/mydeployment -- date
  
  # Get output from running 'date' command from the first pod of the service myservice, using the first container by
default
  kubectl exec svc/myservice -- date

Options:
    -c, --container='':
	Container name. If omitted, use the kubectl.kubernetes.io/default-container annotation for selecting the
	container to be attached or the first container in the pod will be chosen

    -f, --filename=[]:
	to use to exec into the resource

    --pod-running-timeout=1m0s:
	The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one pod is running

    -q, --quiet=false:
	Only print output from the remote session

    -i, --stdin=false:
	Pass stdin to the container

    -t, --tty=false:
	Stdin is a TTY

Usage:
  kubectl exec (POD | TYPE/NAME) [-c CONTAINER] [flags] -- COMMAND [args...] [options]

Use "kubectl options" for a list of global command-line options (applies to all commands).
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl exec -it nginx-api-deployment-746876665c-ttqvc -- /bin/bash
root@nginx-api-deployment-746876665c-ttqvc:/# ip a
bash: ip: command not found
root@nginx-api-deployment-746876665c-ttqvc:/# ifconfig
bash: ifconfig: command not found
root@nginx-api-deployment-746876665c-ttqvc:/# exit    
exit
command terminated with exit code 127
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ #kubectl debug -it nginx-api-deployment-746876665c-ttqvc --image=busybox
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ kubectl debug -it nginx-api-deployment-746876665c-ttqvc --image=busybox
--profile=legacy is deprecated and will be removed in the future. It is recommended to explicitly specify a profile, for example "--profile=general".
Defaulting debug container name to debugger-hbs2z.
All commands and output from this session will be recorded in container logs, including credentials and sensitive information passed through the command prompt.
If you don't see a command prompt, try pressing enter.
/ # ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0@if8: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue 
    link/ether b2:0c:96:c8:15:39 brd ff:ff:ff:ff:ff:ff
    inet 10.244.0.7/24 brd 10.244.0.255 scope global eth0
       valid_lft forever preferred_lft forever
/ # exit
Session ended, the ephemeral container will not be restarted but may be reattached using 'kubectl attach nginx-api-deployment-746876665c-ttqvc -c debugger-hbs2z -i -t' if it is still running
purva@purva-devops:~/work/k8s-launch-pad/infra/k8s$ cd
purva@purva-devops:~$ cd .kube/
purva@purva-devops:~/.kube$ ll
total 20
drwxr-x---  3 purva purva 4096 Nov 27 20:05 ./
drwxr-x--- 46 purva purva 4096 Nov 27 20:04 ../
drwxr-x---  4 purva purva 4096 Nov 27 20:05 cache/
-rw-------  1 purva purva 5582 Nov 27 20:04 config
purva@purva-devops:~/.kube$ cat config 
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUMvakNDQWVhZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJMU1URXlOekUwTXpNMU1Gb1hEVE0xTVRFeU5URTBNek0xTUZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTVB5Cm53Q0luaUpXQXY2WndzSGcvQjh2c3pMWGhrVWl4VnpmUGNJWFI5M3FnWWtUWnRaRXZQbWU3WlVDSmJBTzNnR2QKWDhwY0NRckhaZEp3RCtlMkJXeFVLaTFIaEpuQTFmWExpUUVTZ05FVitxb1h3R3BYN0JMQkV0NTFtK1dSTDJjWgpWaEdROTg1T050UUlqbWZiWEV4UjZrN1FwK25NYWVKL2ZxeXhHWDlIcndYMnV3RE9ZeTlGaFh1ZGthM0VUWDg2ClJlYnkvY2RnbEpNWnZicndrc3dQc0IvWm93eXFnbldtUk4zNlV4c3FpbWxGRW0rZ3NHb09rSVJaQmFsdWxDS3cKcFpNNWN4a0VKa3lsOWxPemJMS0poTVBLTXJVbnNPelovVXFmODVld0hJQzBlbSsrWlh0dDc0bnRSbzUyMEFlYQpRYkF1RjZVZ3AzNVNpYjVWMko4Q0F3RUFBYU5aTUZjd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZEbmdTNHBBTS9reDdUYmp1TGkxekNrbEVaZ1JNQlVHQTFVZEVRUU8KTUF5Q0NtdDFZbVZ5Ym1WMFpYTXdEUVlKS29aSWh2Y05BUUVMQlFBRGdnRUJBTE8xWjc1RHlldEtaYzBmMFBJUwpBQTNaK1ZBcXlZd1d5TTRrVmMyMzFFNlFtKzNwR0daNi8yL29DV3QvazFBRmlTMnNaWlQzQmRaekdpaXMvZjVKClIwc3JaVG5qUGhTTGlrUWxmczFUMWpacm9TSUI4OGhPUXNPWUxaNlp3YnE0dWhUQmpZR0hHellTL2piU05EUVYKTE96cSt1U0FXcDFUV1R3bUFkQnc5eW85VmR1ekFRSEd6aGxKSWFmN3RuOWpuNmpkekExNWdPUW1jMGhaMnhSNQo0QUs3a0d0Z0kwLzRueEl5TlNnRWNWS3RlSmxmNkxqeUFWdU9ZTnIxUUNFNFNvanlFc1pLRlRPMmRFZ1pWVGE3Cms5N0JGMEdMOGt6NTIxd0l2ZkxTMndaUy9SemNDUDVIWUdWM2FyMjE2d21oNUg0SlRoS3ZLRVRHMU1Xa1dScWoKTFRnPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
    server: https://127.0.0.1:35743
  name: kind-kind
contexts:
- context:
    cluster: kind-kind
    user: kind-kind
  name: kind-kind
current-context: kind-kind
kind: Config
preferences: {}
users:
- name: kind-kind
  user:
    client-certificate-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURJVENDQWdtZ0F3SUJBZ0lJRVVoZGdMMTNZSEV3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TlRFeE1qY3hORE16TlRCYUZ3MHlOakV4TWpjeE5ETXpOVEphTURReApGekFWQmdOVkJBb1REbk41YzNSbGJUcHRZWE4wWlhKek1Sa3dGd1lEVlFRREV4QnJkV0psY201bGRHVnpMV0ZrCmJXbHVNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTNpYkgwb1dDcGovQ2xxV0MKR1ZTeHRSaTZyVzFpbzNmT1pqelQxQS9vMXN3TEphbHVHT25QRjAwejNpN1dHZVVnaGMvcTdmcUw1bzZTTkpPKwpQRVd4b1BUK0dNZHI2V2wyKzRwY3hPVmhkblRZTHdURW5wV0drbzNrZWNLUXpvQytiZkhPbUlucjg4cWtGOWlWCnFuVVVlWll1bGh3cEhyNS9sMkp5U1RVdlpla2h6MG1Jd1lXbGJBQUtCY1doOTJrdWR5ZVlrdWVyR2trc2RzN3kKRmhUSUZSdGVrdWk0aEQxbm9KQ0prUk83ZUtpMmhJSFF2QmlleW9HREpsUWxqQVBTSVZicExyODVKYVJONXJ0VgprcFNLZnJ6MFNrRm9vdG1sbjA2VFNYN2RYZVVPRWtRVUhuLzRtdEQwUFJ0azdFYk5FbUtZcVBuWWx1SWtOVEs4Ci9TSUM4UUlEQVFBQm8xWXdWREFPQmdOVkhROEJBZjhFQkFNQ0JhQXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUgKQXdJd0RBWURWUjBUQVFIL0JBSXdBREFmQmdOVkhTTUVHREFXZ0JRNTRFdUtRRFA1TWUwMjQ3aTR0Y3dwSlJHWQpFVEFOQmdrcWhraUc5dzBCQVFzRkFBT0NBUUVBRmZpWkZnN0NwMkJmMW9CNjZhN2c0eENEd0lrUEJCbnJtNm9RCkE3djQrS1hZU2o1V3Jyc0d2dUN1Tktra3Q2SEhCUmFXSzloZ3Mrd2gxU0pUZ3FlbVpnK1lydGREV2ptdDZpWkcKVTEyYUVjb09kbC90OGxzbG1YTndRYXA0M1NqeWx0VE9IMXNUZzUxQXo3TjlhaDdCUFE5ME5UTDZoNzFYZmtDTQpDYWhnMkNFbTNYN0hxNVIyYUg1dW90NENTRVl5WWNTMTZiOXlBK0tPcW5jY2wrT1JvbnhiMFhSMHN2TmRDUTJTCktCZkVIb2Fzd2FITEhCekMvVjlqbTZGRWpVRElDTVFsVDNCNUVMZTgvdmFWNVBqMEJaUDFWcG0zTTRzYmp3K2gKd3M4ZXA2QlI1ek1aMExmOFluQUFtZ2UxbXg3eEFVb3Fzd04ydG1ZVlZqeW9aanpxN3c9PQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
    client-key-data: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVBM2liSDBvV0Nwai9DbHFXQ0dWU3h0Umk2clcxaW8zZk9aanpUMUEvbzFzd0xKYWx1CkdPblBGMDB6M2k3V0dlVWdoYy9xN2ZxTDVvNlNOSk8rUEVXeG9QVCtHTWRyNldsMis0cGN4T1ZoZG5UWUx3VEUKbnBXR2tvM2tlY0tRem9DK2JmSE9tSW5yODhxa0Y5aVZxblVVZVpZdWxod3BIcjUvbDJKeVNUVXZaZWtoejBtSQp3WVdsYkFBS0JjV2g5Mmt1ZHllWWt1ZXJHa2tzZHM3eUZoVElGUnRla3VpNGhEMW5vSkNKa1JPN2VLaTJoSUhRCnZCaWV5b0dESmxRbGpBUFNJVmJwTHI4NUphUk41cnRWa3BTS2ZyejBTa0Zvb3RtbG4wNlRTWDdkWGVVT0VrUVUKSG4vNG10RDBQUnRrN0ViTkVtS1lxUG5ZbHVJa05USzgvU0lDOFFJREFRQUJBb0lCQUFNL1VlQno3eXI2OTU4NApJQ1M2cGpaZGZDMFkwajVOZkFqbWpyb2syV1I2YXhkTDJMNG9mTXg4Wm11ekI1SXRWVUpmZmJHbzNlNnEydHhGCjVKd0E4TTNIaHdkWnN1d2dqSXEweFJKanYvNzVTa2UxckNJZFVYQkcvcllBOEJqMHJOUHltdkNENDUwV3N6dGUKQVNJU3dBL2U4Q05sbWZ4SEVKcG41Ly9GOVVGcUZnbG9PZGI0aEw5SlZKWnA1SVc1QlJMVVFHMlpqN0VlTXFhSQp4SUdsMkpnTXdKYTdjbDFyTy81Qytaa0c0OWRHaWZOTjRWWHZEUXhiVVk5NHFqQXVaY3Q1elJGOEZzeEI3cnlECi92WmhTSFpxZjFIZlFyeHl3OGlRLzEvVkhuZXh3a1pmZVp6RGZJQnJJMHB3MEJNTmdWMW54dFZkTWxJK2YvSngKRU96N0pSa0NnWUVBNncrM2htNkY3dDFzWjgxaGhaVzBpTzZtMCtYd3Zaanl0bktxU1QzdmR4N2pkd1VrYTRuQwpFc1Jzalo2K1FRNUxkYzRsK3FhbEdOM2FoRFBrVXg1ZTc1VFozcXhwcTVZWXJXM0ZpZjRuemV1bEpFTUNFSDhiCnQ1Rjd0d082dXZKS2xEVjJXOEVYY1VwVDNoQjQ0dWEySC9GWC80UFo1cnB2enMwT0hHTC9qNk1DZ1lFQThmQ3IKVkU4cGVhNmZiTmdQODkzUjFCSUpRQ3dxYklXa2pWWVJyUUpGMmxlcGtpNFhZWmN1aHp1TVBTWUxmaHpFbTV3MwpVcWphOFlHcU9ZWnJHbG8vV0xJQitSQXdFUEVuYTNGSVBWRUUxQ3V3TTFZd3dHODdkb1JESEM4d0F6UitzV2psClBXRGJHTFdZYTh4b0haVG92NWRpTHdVTXllMVVXbi9zSlNIZGZGc0NnWUJRSkNPbUtiaHdILzM5eGdBaDAxQ2gKL3Z2Ujh1dUpPTVJIZ0FDZXlBY0V6ZnN2Y1FsaHdLM3lTQlhha3V5NnNXejQxVGdOcFJOVXp3N1pVL2ZjZnRaUApTS2lmU3BrY2J5Z3F1T3BJaWVaNFJvY2ZQZGxPVm9mVXBqMVB3RzNCbnluZUxmd1VmRmpKdjFXb3VHVCt0em9RCjJlL3VwYjE4OU1ONTlsK0JQaDl6a1FLQmdBb0d5MUxuSlBUaUE4RmpBdVk4WHlIR3paTlhRVHJXSHdlc2RYY1MKRFFzTGJ2K2I0V1F0KzhPbStCemdvc0ZMTitxckFxL3VSNFNTdHhkRE50VVV3R05RblR4UksyeklVYlhtTC9RNgprMVNucXRtMXpMZHM1SzM0dFQ5SnhWZWNxVk40NFdjMXlGNnh4K3RQd1ZEWWh2ekpyVXY5alpZZ3U4bzBXdmorCitrclpBb0dCQU5JTWczRlZ6VCtSWlhyZm11WmgyL3pBcGtjYzRCWlFjWTRNS283SUNKVWRoRkZsSDdtVStuOUUKdlUweXBTSXdRUERyZzZLL2JSSFRPUGZ1aUkvUyt5Q1FpOE1aWHQ4TmhHdi9UQVI1YlZvRHk1M1BMeElRdS9Ebwpyd0NVR2dkbkd6d2RaMEI2Wk9GMi9oaEpQVmYwWTc4djJqQ3p2b2hIaHVMRk12aHhuZndWCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg==
purva@purva-devops:~/.kube$ 
