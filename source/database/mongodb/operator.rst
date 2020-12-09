基本操作
========

索引操作
--------

.. code-block:: bash

    # 创建索引
    db.collection_name.ensureIndex({"key_name":1})

    # 创建唯一索引
    db.collection_name.ensureIndex({"key_name":1},{"unique":true})

    # 复合唯一索引
    db.collection_name.ensureIndex({'key1':1, 'key1':1})

    # 10s后自动删除
    db.collection_name.ensureIndex({"key_name":1},{expireAfterSeconds:10})


增删改查
--------

.. code-block:: bash

    # 查找
    db.getCollection('collection_name').find({"provison_state": "success"})

    # 使用正则表达式
    db.getCollection('collection_name').find({"date": /2020-01-/})

    # range
    db.getCollection('collection_name').find({"date": {"$gt": ISODate("2020-07-18T00:00:00.000Z")}})

    # 删除文档
    db.getCollection('collection_name').remove({"provison_state": "success", "industry": null})

    # 删除集合中所有文档
    db.getCollection('collection_name').remove({})

更新子文档
----------


通过id获取时间
--------------

mongodb 的 Objectid 由12字节构成，分别是：

- a 4-byte value representing the seconds since the Unix epoch,
- a 3-byte machine identifier,
- a 2-byte process id, and
- a 3-byte counter, starting with a random value.

.. code-block:: bash

    ObjectId("567a68517507b377a0a20903").getTimestamp()


分页
----

.. code-block:: bash

    # Page 1
    db.getCollection('collection_name').find({}).limit(5)

    # Page 2
    db.getCollection('collection_name').find({}).skip(5).limit(5)

    # Page 3
    db.getCollection('collection_name').find({}).skip(10).limit(5)