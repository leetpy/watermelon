Ansible
=======

解决 ssh 首次登录认证问题

在脚本执行目录下添加 `ansible.cfg` 文件，内容如下：

.. code-block::

   [defaults]
   host_key_checking = False