
集群配置
========

修改 node-port 端口范围：

#. 在 `/etc/kubernetes/manifests/kube-apiserver.yaml` 文件中增加 `service-node-port-range` 参数；
#. systemctl restart kubelet；

.. code-block:: yaml

   apiVersion: v1
   kind: Pod
   metadata:
     creationTimestamp: null
     labels:
       component: kube-apiserver
       tier: control-plane
     name: kube-apiserver
     namespace: kube-system
   spec:
     containers:
     - command:
       - kube-apiserver
       - --advertise-address=192.168.0.254
       - --allow-privileged=true
       - --authorization-mode=Node,RBAC
       - --client-ca-file=/etc/kubernetes/pki/ca.crt
       - --enable-admission-plugins=NodeRestriction
       - --enable-bootstrap-token-auth=true
       - --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt
       - --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt
       - --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key
       - --etcd-servers=https://127.0.0.1:2379
       - --insecure-port=0
       - --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt
       - --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key
       - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
       - --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt
       - --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key
       - --requestheader-allowed-names=front-proxy-client
       - --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.crt
       - --requestheader-extra-headers-prefix=X-Remote-Extra-
       - --requestheader-group-headers=X-Remote-Group
       - --requestheader-username-headers=X-Remote-User
       - --secure-port=6443
       - --service-account-key-file=/etc/kubernetes/pki/sa.pub
       - --service-cluster-ip-range=10.1.0.0/16
       - --service-node-port-range=1-65535

