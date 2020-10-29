etcd 介绍
=========

etcd 官方的定义是："一个分布式，可靠的关键数据 kv 存储"。

特性
----

#. 接口简单，采用标准的 http 协议，json 传输;
#. 数据存储在分层的目录结构；
#. 可监控指定key 或者目录变化;
#. 支持 SSL 认证;
#. 单机每秒 1000 的写入;
#. 支持 key TTLs 过期;
#. 采用 Raft 算法;

关于 Raft 算法可以参考： http://thesecretlivesofdata.com/raft/


