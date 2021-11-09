内置函数
========

- ans()

- absent()

- absent_over_time()

- ceil()

- changes()

- clamp()

- clamp_max()

- clamp_min()

- day_of_month()

- day_of_week()

- days_in_month()

- delta()

- deriv()

- exp()

- floor()

- histogram_quantile()

- holt_winters()

- hour()

- idelta()

- increase()

- irate()

- label_join()

- label_replace()

- ln()

- log2()

- log10()

- minute()

- month()

- predict_linear()

- rate()

  `rate(v range-vector)` 计算区间数据每秒的平均值。

  eg: 获取最近 5min 的 QPS

  .. code-block::

     rate(http_requests_total{job="api-server"}[5m])

  `rate` 应该只用于 `Counter` 类型的数据。

- resets()

- round()

- scalar()

- sgn()

- sort()

  `sort(v instant-vector)` 按递增顺序排

- sort_desc()

  逆序排

- sqrt()

- time()

- timestamp()

- vector()

- year()

- aggregation>_over_time()