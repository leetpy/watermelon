主从同步
========


.. code-block:: bash

    # 如果主服务设置了密码
    config set masterauth <pwd>

    # 设置主服务器
    SLAVEOF 192.168.1.100 6379

    # 取消同步
    SLAVEOF NO ONE
