数据迁移
========


.. code-block:: bash

   # 导出所有数据库
   mysqldump -uroot -p123456 --all-databases > all.sql

   # 新环境导入
   mysql -uroot -p123456 < all.sql

   # 导出指定的数据库
   mysqldump -uroot -p123456 mydb > mydb.sql

   # 导入
   mysql -uroot -p123456 mydb < mydb.sql

   # 导出指定表的数据
   mysqldump -uroot -p123456 mydb mytable > mytable.sql

   # 导入
   mysql -uroot -p123456 mydb < mytable.sql