创建 harbor 认证
=================


.. code-block:: bash

    kubectl create secret docker-registry harbor --namespace=ns --docker-server=https://your.harbor.cn --docker-username=username --docker-password=password
