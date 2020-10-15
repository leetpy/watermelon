常用操作
========

Host授权
---------

.. code-block:: sql

    -- 通配符设置网段
    grant all privileges on <db_name>.* to root@'10.10.10.%' identified by '<pwd>';

    grant all privileges on *.* to root@'10.10.10.100' identified by '<pwd>';
    flush privileges;