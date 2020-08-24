基本语法
========

术语
----

1. Node / 节点
2. Member / 成员


语法
----

这里全部用 V3 版本

.. code-block:: bash

    # 设置api 版本
    export ETCDCTL_API=3

    # 设置key
    etcdctl put /monitor_services/thalassa/uri/relay_exist 0.5

    # 获取key对应的值
    etcdctl get /monitor_services/thalassa/uri/relay_exist

    # 只打印值，不打印key
    etcdctl get /monitor_services/thalassa/uri/relay_exist --print-value-only

    # 匹配key 列表
    etcdctl  get /monitor_services/thalassa/uri/ --prefix --keys-only

    # 监控key是否发生变化
    etcdctl watch foo

    # 监控匹配key
    etcdctl watch --prefix foo

