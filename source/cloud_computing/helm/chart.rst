Charts
======

.. code-block:: bash

    # 创建 Chart
    helm create myapp

    # 检查
    helm lint myapp

    # 打包
    helm package myapp

    # 上传文件到 helm repo (artifactory 仓库)
    curl -u username:password -T myapp-0.1.0.tgz "https://xxx/artifactory/my-helm-release/myapp-0.1.0.tgz"

    # 安装 Chart
    helm install <name> <package>

    # 删除 Chart
    helm uninstall <name>