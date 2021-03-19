Cli
===

集群相关

.. code-block:: console

   $ openstack availability zone list
   +-----------+-------------+
   | Zone Name | Zone Status |
   +-----------+-------------+
   | internal  | available   |
   | nova      | available   |
   +-----------+-------------+

认证

.. code-block:: bash

   # 列出所有的用户
   openstack user list

   # 列出认证服务目录
   openstack catalog list

实例

.. code-block:: bash

   # 列出实例，核实实例状态
   openstack server list

   # 列出规格类型
   openstack flavor list

   # 删除实例
   openstack server delete bad544b4-46df-4b0a-9067-a1c680b687c9

   # 显示实例详细信息
   openstack server show NAME

   # 查看云主机的控制台日志
   openstack console log show MyFirstInstance

网络

.. code-block:: console

   $ openstack network list
   +--------------------------------------+---------+--------------------------------------+
   | ID                                   | Name    | Subnets                              |
   +--------------------------------------+---------+--------------------------------------+
   | 80b79915-3ae5-484b-8b9f-32429dde3cfb | private | c34d7720-2bd5-42bf-93f6-c88f3b57ceb8 |
   | e9e3b8d8-9ef1-4438-814e-482d2bceffe9 | public  | 57f6f7a9-ee60-4368-8416-8b61346a9d7f |
   +--------------------------------------+---------+--------------------------------------+

镜像

.. code-block:: console

   $ openstack image list
   +--------------------------------------+--------------+--------+
   | ID                                   | Name         | Status |
   +--------------------------------------+--------------+--------+
   | d06fd808-81bb-4e38-aea3-601a20cb96bd | cirros       | active |
   | 2318e35b-72f2-444d-98a8-24f586aab347 | cirros-0.3.1 | active |
   +--------------------------------------+--------------+--------+

卷

.. code-block:: console

   $ openstack volume list
   +--------------------------------------+------+-----------+------+-------------+
   | ID                                   | Name | Status    | Size | Attached to |
   +--------------------------------------+------+-----------+------+-------------+
   | 6b378e55-ab2b-4ccf-a2d2-47b3c5c212f1 |      | available |    1 |             |
   +--------------------------------------+------+-----------+------+-------------+