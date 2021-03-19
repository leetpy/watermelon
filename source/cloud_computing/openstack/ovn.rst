ovn
===

ovn-controller
--------------

ovs-vswitchd 的Openflow 控制器来控制流量的转发。ovn-controller是一种分布式SDN控制器。



ovn-northd
-----------


neutron & ovn
-------------

使用neutron创建的网络在ovn上以switch形式存在

.. code-block:: console

   # ovn-nbctl show
   switch e90a7858-68d5-49bd-90f6-844863ecd511 (neutron-4f362a66-81ff-4784-8297-6a411c68c58b) (aka net1)
       port 0c30be97-9757-4d1b-91a1-7428f22e051b
           type: localport
           addresses: ["fa:16:3e:b1:83:1b 192.168.1.2"]
       port 699211f0-dbd5-42d1-9097-ebaf104f1893
           addresses: ["fa:16:3e:5b:b7:c7 192.168.1.239"]
       port provnet-4f362a66-81ff-4784-8297-6a411c68c58b
           type: localnet
           tag: 100
           addresses: ["unknown"]


neutron创建出的port在对应OVN网络的switch上以port形式存在，在OVS上以port形式存在


查看 bridge_mapping 信息

.. code-block:: console

   # ovs-vsctl get Open_vSwitch . external-ids:ovn-bridge-mappings
   "extnet:br-ex,physnet1:br-data"