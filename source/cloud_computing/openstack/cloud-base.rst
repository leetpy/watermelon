cloud-base
==========

常用配置
--------

#. 配置获取metadata的重试次数和间隔

   修改 `C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf\cloudbase-init.con` 文件:

   .. code-block::

      retry_count=40
      retry_count_interval=5