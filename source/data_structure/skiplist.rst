跳表
====

跳表的本质是在链表的基础上建立多级索引，如下图所示：

.. image:: images/Skiplist.png

跳表操作：

#. 插入
#. 删除
#. 查找
#. 查找一个区间的元素
#. 输出有序序列


为啥redis 使用跳表，不使用红黑树:

#. 跳表操作时间复杂度和红黑树相同;
#. 跳表代码实现更易读;
#. 跳表区间查找效率更高


