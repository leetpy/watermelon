连接数
======

.. code-block:: bash

   # 设置最大连接数量
   set GLOBAL max_connections=100;

   # 查看最大连接数
   show variables like 'max_connections';

   # 查看已使用的连接数
   show global status like 'Max_used_connections';