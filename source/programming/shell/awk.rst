awk
===

.. code-block:: bash

    # 求和
    awk '{sum += $1};END {print sum}'

    # 字符串转 int
    awk '{print int($1)}'