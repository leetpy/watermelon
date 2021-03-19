Neutron
========


网络

.. code-block:: bash

   # 创建 vlan 网络
   neutron net-create <name> --shared --provider:physical_network physnet1  --provider:network_type vlan --provider:segmentation_id 16