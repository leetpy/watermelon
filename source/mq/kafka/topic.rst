Topic
=====

topic 相关操作
---------------

.. code-block:: bash

   # 创建 topic
   ./kafka-topics.sh --create --zookeeper localhost:2181/kafka --replication-factor 1 --partitions 1 --topic test

   # 列出所有 topic
   ./kafka-topics.sh --zookeeper localhost:2181/kafka --list

   # 查看 topic
   ./kafka-topics.sh --zookeeper localhost:2181 --describe --topic test

   # 增加分区数量 (分区只能增加不能减少)
   ./kafka-topics.sh --zookeeper localhost:2181 --alter --topic test --partitions 4