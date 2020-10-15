prometheus
==========

使用
----

prometheus 是拉模式的，如果要向 prometheus 发送数据，可以先发送到 pushgateway, 然后再配置 prometheus 拉取 pushgateway 的数据。


https://github.com/prometheus/pushgateway

metrics
--------


数据类型
^^^^^^^^

#. Counter

   Counter 是计数器，单调递增的，只有服务重启时才会清零。

#. Guage

#. Historgram

#. Summary

疑问
----

#. 服务down机重启 Counter 会重新计数；
#. 起多个进程，Counter 错乱；