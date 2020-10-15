消息确认机制
============

1. 确认消息是否发送到 broker;
2. 确认消息是否成功消费;

RabbitMQ为我们提供了两种方式：

通过AMQP事务机制实现，这也是AMQP协议层面提供的解决方案；
通过将channel设置成confirm模式来实现；

事务机制
--------

RabbitMQ中与事务机制有关的方法有三个：txSelect(), txCommit()以及txRollback(),
txSelect用于将当前channel设置成transaction模式，txCommit用于提交事务，txRollback用于回滚事务，在通过txSelect开启事务之后，
我们便可以发布消息给broker代理服务器了，如果txCommit提交成功了，则消息一定到达了broker了，
如果在txCommit执行之前broker异常崩溃或者由于其他原因抛出异常，这个时候我们便可以捕获异常通过txRollback回滚事务了。


Confirm模式
-----------

使用事物可以确认消息是否真的到达 broker, 但是会影响系统的吞吐量，使用Confirm可以解决这一问题。