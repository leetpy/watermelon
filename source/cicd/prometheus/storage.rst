数据存储
========



Prometheus 内置了一个本地的时序数据库，同时也支持配置远端数据库。

本地存储
--------

.. code-block::

   ./data
   ├── 01BKGV7JBM69T2G1BGBGM6KB12
   │   └── meta.json
   ├── 01BKGTZQ1SYQJTR4PB43C8PD98
   │   ├── chunks
   │   │   └── 000001
   │   ├── tombstones
   │   ├── index
   │   └── meta.json
   ├── 01BKGTZQ1HHWHV8FBJXW1Y3W0K
   │   └── meta.json
   ├── 01BKGV7JC0RY8A6MACW02A2PJD
   │   ├── chunks
   │   │   └── 000001
   │   ├── tombstones
   │   ├── index
   │   └── meta.json
   ├── chunks_head
   │   └── 000001
   └── wal
       ├── 000000002
       └── checkpoint.00000001
           └── 00000000

远程存储集成
------------