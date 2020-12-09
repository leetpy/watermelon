Virsh
=====

virsh 是 libvirt 的 cli 工具，通过调用 libvirt 接口来控制虚拟机。


- 常用命令

  .. code-block:: console

     # 查看虚机列表
     $ virsh list
     Id    Name                           State
     ----------------------------------------------------
      3     dev_test                       running

     # 查看网络
     $ virsh net-list

     # dumpxml
     $ virsh dumpxml <id>

     # 查看 vnc 端口号
     $ virsh vncdisplay <id>

     # 增加网卡
     $ virsh attach-interface --domain vm1 --type bridge --source br1