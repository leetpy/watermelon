分片
====

分片大小设计规则
-----------------

按照 20-50G 一个分片划分比较合适。


#. 查看分片分布情况

   http://localhost:9200/test_index/_search_shards
