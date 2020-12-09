repo
====

.. code-block:: bash

    # 添加 repo
    helm repo add my-helm-repo https://xxx/artifactory/my-helm-virtual --username <username> --password <password>

    # 更新 repo
    helm repo update


.. NOTE::

    helm repo 的信息是存在 `$HOME/.helm` 目录下的，所以切换用户后， helm repo 信息是看不到的。