随机抽奖算法
=============

题目：

从 1- n 中随机抽取 k 个数。


.. code-block:: python

   from random import randint

   def sample(population, k):
       result = [None] * k
       pool = list(population)
       n = len(population)
       for i in range(k):
           j = randint(0, n-i)
           result[i] = pool[j]
           pool[j] = pool[n-i-1]  # 把末尾的元素移动到抽出的位置

       return result