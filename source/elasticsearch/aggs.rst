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

