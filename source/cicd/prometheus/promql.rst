PromQL
======

PromQL (Prometheus Query Language) 是 Prometheus 自己开发的数据查询 DSL 语言，
语言表现力非常丰富，内置函数很多，在日常数据可视化以及rule 告警中都会使用到它。

查询结果类型
--------------

PromQL 查询结果主要有 3 种类型：

- 瞬时数据 (Instant vector): 包含一组时序，每个时序只有一个点，例如：http_requests_total
- 区间数据 (Range vector): 包含一组时序，每个时序有多个点，例如：http_requests_total[5m]
- 纯量数据 (Scalar): 纯量只有一个数字，没有时序，例如：count(http_requests_total)

查询条件
--------

Prometheus 存储的是时序数据，
而它的时序是由名字和一组标签构成的，
其实名字也可以写出标签的形式，
例如 http_requests_total 等价于 `{name="http_requests_total"}`。

操作符
------

Prometheus 查询语句中，支持常见的各种表达式操作符，例如

#. 算术运算符

   支持的算术运算符有 +，-，*，/，%，^,
   例如 http_requests_total * 2 表示将 http_requests_total 所有数据 double 一倍。

#. 比较运算符

   支持的比较运算符有 ==，!=，>，<，>=，<=,
   例如 http_requests_total > 100 表示 http_requests_total 结果中大于 100 的数据。

#. 逻辑运算符

   支持的逻辑运算符有 and，or，unless,
   例如 http_requests_total == 5 or http_requests_total == 2
   表示 http_requests_total 结果中等于 5 或者 2 的数据。

#. 聚合运算符

   sum，min，max，avg，stddev，stdvar，count，count_values，bottomk，topk，quantile，
   例如 max(http_requests_total) 表示 http_requests_total 结果中最大的数据。


内置函数
--------

Prometheus 内置不少函数，方便查询以及数据格式化，
例如将结果由浮点数转为整数的 floor 和 ceil，

.. code-block:: bash

   floor(avg(http_requests_total{code="200"}))
   ceil(avg(http_requests_total{code="200"}))



.. code-block:: bash

   sum(rate(http_server_requests_seconds_count{job="presell-pro", uri="/helloWorld"}[5m])) by (uri)
