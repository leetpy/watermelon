聚合
====


.. code-block:: bash

    # 按 key 排序
    "total_use": {
        "terms": {
            "field": "total_use",
            "size": 100,
            "order": {
                "_term": "desc"
            }
        }
    }


聚合排序

.. code-block:: bash

   {
      "query": {},
      "aggs": {
          "frame_id": {
              "terms": {
                  "field": "frame_id",
                  "size": 10,
                  "order": {
                      "relation_id": "desc"
                  }
              },
              "aggs": {
                  "relation_id": {
                      "cardinality": {
                          "field": "relation_id"
                      }
                  }
              }
          }
      }
   }

聚合分区
--------

如果聚合的结果太多，一次返回会非常慢，可以将结果分块，然后每次返回一部分。

.. code-block:: json

   {
      "size": 0,
      "aggs": {
         "expired_sessions": {
            "terms": {
               "field": "account_id",
               "include": {
                  "partition": 0,
                  "num_partitions": 20
               },
               "size": 10000,
               "order": {
                  "last_access": "asc"
               }
            },
            "aggs": {
               "last_access": {
                  "max": {
                     "field": "access_date"
                  }
               }
            }
         }
      }
   }

.. NOTE::
    如果指定了一个很大的分区数量，而聚合的结果很少，返回的结果是在随机分区，而不是第一个或者最后一个分区。

常规做法：

#. 使用 `cardinality` 统计总的数据，从而计算分区数量；
#. 依次获取每个分区的数据；