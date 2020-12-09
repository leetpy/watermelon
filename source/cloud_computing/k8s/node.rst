节点管理
========

节点操作

.. code-block:: bash

    # 驱赶节点上所有 pod
    kubectl drain 192.168.100.102 --delete-local-data --ignore-daemonsets

    # 删除节点
    kubectl delete node

    # 生成加入集群命令 （master 上执行）
    kubeadm token create --print-join-command


label 操作

.. code-block:: bash

    # 显示 label
    kubectl get nodes --show-labels

    # 添加 label
    kubectl label nodes <node-name> <label-key>=<label-value>

    # 删除 label
    kubectl label nodes <node-name> <label-key>-

    # 修改 label
    kubectl label nodes <node-name> <label-key>=<label-value> --overwrite

使用 label 调度

.. code-block:: yaml

   apiVersion: apps/v1beta1
   kind: Deployment
   metadata:
     name: nginx
   spec:
     replicas: 1
     template:
       metadata:
         labels:
           app: nginx
       spec:
         containers:
         - name: nginx
           image: nginx:latest
         nodeSelector:
           label_name: label_value
