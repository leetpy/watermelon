LLDP查询网络拓扑
====================

#. 安装工具包

   .. code-block:: bash

      yum install lldpd
      systemctl start lldpd


#. 查询lldp 信息

   .. code-block:: console

      # lldpcli show neighbors
      -------------------------------------------------------------------------------
      LLDP neighbors:
      -------------------------------------------------------------------------------
      Interface:    eth0, via: LLDP, RID: 1, Time: 0 day, 00:01:58
        Chassis:
          ChassisID:    mac 00:00:00:00:00:00
          SysName:      xxx
          SysDescr:     H3C Comware Platform Software, Software Version 7.1.070, Release 1312
                        H3C S5130-54C-HI
                        Copyright (c) 2004-2019 New H3C Technologies Co., Ltd. All rights reserved.
          MgmtIP:       10.95.85.1
          Capability:   Bridge, on
          Capability:   Router, on
        Port:
          PortID:       ifname GigabitEthernet1/0/25
          PortDescr:    GigabitEthernet1/0/25 Interface
          TTL:          121

FAQ
---

#. intel X710 lldp agent 禁用

   .. code-block:: bash

      # 查看 driver 是否是 i40e
      ethtool -i eth0 | grep "driver"

      # disable lldp agent，注意 0000:01:00.2 是 pci 号，可以先 cat, 里面会显示网卡的名字
      echo lldp stop > /sys/kernel/debug/i40e/0000:01:00.2/command