go陷阱
======

1. make slice 时指定len;

   eg:

   .. code-block:: go

    // 指定 len 和 cap 都为10
    var docs []string = make([]string, 10, 10)

   这个时候 docs 已经有十个已经初始化的值了，进行append 操作时，不会删除原来的值，
   正确做法是指定 len 为0，cap 为我们希望的大小。