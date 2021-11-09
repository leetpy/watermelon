OpenStack 命令行速查表
=========================


认证(keystone)

.. code-block:: bash

   # 列出所有的用户
   openstack user list

   # 列出认证服务目录
   openstack catalog list

   # AZ
   openstack availability zone list

计算(nova)

.. code-block:: bash

   # 列出规格类型
   openstack flavor list

   # 创建 flavor
   openstack flavor create --ram 512 --disk 1 --vcpus 1 m1.tiny

   # 列出实例，核实实例状态
   openstack server list

   # 删除实例
   openstack server delete bad544b4-46df-4b0a-9067-a1c680b687c9

   # 显示实例详细信息
   openstack server show NAME

   # 查看云主机的控制台日志
   openstack console log show MyFirstInstance

   # 指定 user-data
   openstack server create --user-data userdata.txt --image cirros-qcow2 --flavor m1.tiny MyUserdataInstance2

网络(neutron)

.. code-block:: bash

   # 网络列表
   openstack network list

   # 创建安全组
   neutron security-group-rule-create --direction ingress --ethertype IPv4 my_sg

   # 创建 VLAN 网络
   neutron net-create net1 --shared --provider:physical_network physnet1 --provider:network_type vlan --provider:segmentation_id 16


镜像(glance)

.. code-block:: bash

   # 镜像列表
   openstack image list

   # 显示进度
   glance image-create --name windows7 --visibility public --disk-format qcow2 --container-format bare --file win7.qcow2 --progress

   # 设置 VGA
   glance image-create --name centos8 --visibility public --disk-format qcow2 --container-format bare --file centos8.qcow --property hw_video_model=vga --progress

卷(cinder)

.. code-block:: bash

   # 卷列表
   openstack volume list


对象存储(swift)

.. code-block:: bash

   # 列出容器
   swift list

   # 展示账户，容器以及对象的信息
   swift stat CONTAINER


swift-ring-builder

.. code-block:: bash

   # 必须到 ring 对应的目录下执行才行
   cd /etc/swift
