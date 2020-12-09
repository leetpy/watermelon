Group
=====


group 相关操作
----------------

.. code-block:: bash

   # 列出所有 consumer group
   ./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list

   # 某个 consumer group 信息
   ./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group_id_qa

   # 将某个 group 的 topic 重置到 earliest
   ./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group example --topic test --execute --reset-offsets --to-earliest