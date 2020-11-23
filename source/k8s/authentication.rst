用户认证
========

生成登录配置文件

.. code-block:: bash

    kubectl config set-cluster kubernetes --server=<master ip>:6443 --kubeconfig=<filename>

    # 这里的scret参数需要替换成上面获取到的登陆的token值
    kubectl config set-credentials dashboard --token="<your token>" --kubeconfig=<filename>

    kubectl config set-context dashboard@kubernetes --cluster=kubernetes --user=dashboard --kubeconfig=<filename>
    kubectl config use-context dashboard@kubernetes  --kubeconfig=<filename>