常用操作
========

.. code-block:: sql

   -- mysql 8.0 以上八版本
   CREATE DATABASE mydatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

   -- 低版本
   CREATE DATABASE mydatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


Host授权
---------

.. code-block:: sql

    -- 通配符设置网段
    grant all privileges on <db_name>.* to root@'10.10.10.%' identified by '<pwd>';

    grant all privileges on *.* to root@'10.10.10.100' identified by '<pwd>';
    flush privileges;