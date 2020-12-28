延时队列
========

核心代码:

.. code-block:: python

   def delay(msg):
       msg.id = str(uuid.uuid4())
       value = json.dumps(msg)
       retry_ts = time.time() + 5  # 5s 后重试
       redis.zadd("delay-queue", retry_ts, value)


   def loop():
       while True:
           # 最多取 1 条
           values = redis.zrangebyscore("delay-queue", 0, time.time(), start=0, num=1)
           if not value:
               time.sleep(1)
               continue
           value = values[0]
           success = redis.zrem("delay-queue", value)
           if success:
               msg = json.load(value)
               handle_msg(msg)