认证
====


.. code-block:: bash

   # 添加 root 用户
   etcdctl --endpoints=http://127.0.0.1:2379 user add root

   # 开启认证
   etcdctl --endpoints=http://127.0.0.1:2379 auth enable

   # 关闭认证
   etcdctl --endpoints=http://127.0.0.1:2379 --user=root:123456 auth disable

   # 创建普通用户
   etcdctl --endpoints=http://127.0.0.1:2379 --user=root:123456 user add guest

   # 添加角色
   etcdctl --endpoints=http://127.0.0.1:2379 --user=root:123456 role add normal

   # 角色授权
   etcdctl --endpoints=http://127.0.0.1:2379 --user=root:123456 role grant-permission --prefix=true normal readwrite /path_name

   # 用户绑定角色
   etcdctl --endpoints=http://127.0.0.1:2379 --user=root:123456 user grant-role guest normal
