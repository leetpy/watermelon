系统
----

进程分析
--------

.. code-block:: bash

    # 查看僵尸进程
    ps -A -ostat,ppid,pid,cmd |grep -e '^[Zz]'
