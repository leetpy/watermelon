存储引擎
========

InnoDb
------
页（Page）是 Innodb 存储引擎用于管理数据的最小磁盘单位。
常见的页类型有数据页、Undo 页、系统页、事务数据页等，
本文主要分析的是数据页。默认的页大小为 16KB，每个页中至少存储有 2 条或以上的行记录，
本文主要分析的是页与行记录的数据结构，有关索引和 B-tree 的部分在后续文章中介绍。

下图是 Innodb 逻辑存储结构图，从上往下依次为：
Tablespace、Segment、Extent、Page 以及 Row。本文关注的重点是 Page 和 Row 的数据结构。

.. image:: images/header.jpg

.. image:: images/struct.jpg

上图为 Page 数据结构，File Header 字段用于记录 Page 的头信息，
其中比较重要的是 FIL_PAGE_PREV 和 FIL_PAGE_NEXT 字段，
通过这两个字段，我们可以找到该页的上一页和下一页，
实际上所有页通过两个字段可以形成一条双向链表。
Page Header 字段用于记录 Page 的状态信息。
接下来的 Infimum 和 Supremum 是两个伪行记录，
Infimum（下确界）记录比该页中任何主键值都要小的值，
Supremum （上确界）记录比该页中任何主键值都要大的值，这个伪记录分别构成了页中记录的边界。


.. image:: images/page.jpg

User Records 中存放的是实际的数据行记录，具体的行记录结构将在本文的第二节中详细介绍。
Free Space 中存放的是空闲空间，
被删除的行记录会被记录成空闲空间。
Page Directory 记录着与二叉查找相关的信息。
File Trailer 存储用于检测数据完整性的校验和等数据。


行格式
^^^^^^
Innodb 存储引擎提供了两种格式的行记录：Compact 和 Redundant。

COMPACT 行格式
""""""""""""""


Redundant 行记录
"""""""""""""""""
