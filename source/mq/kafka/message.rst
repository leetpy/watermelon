Message
========


.. code-block:: bash

   # 发送消息
   ./kafka-console-producer.sh --broker-list localhost:9092 --topic test

   # 消费消息
   ./kafka-console-consumer.sh  --bootstrap-server localhost:9092 --topic test --from-beginning

   # 消费一条消息
   ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --max-messages 1

   # 指定 group 消费一条消息
   ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --group g_group --topic test --max-messages 1