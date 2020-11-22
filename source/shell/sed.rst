sed
===

匹配空格
--------

.. code-block:: bash

    sed -i 's/key[[:space:]]*=[[:space:]]*value/key=new_value/' file


行范围
------

.. code-block:: bash

    # 匹配行到最后一行
    sed -n '/Installed Packages/,$'p file.txt

    # 前两行
    sed -n '1,2'p file.txt

    # 去掉第一行
    sed -n '2,$'p file.txt


模糊匹配
--------

.. code-block:: bash

    # 替换 *.iso 为 test.iso, 注意引号的区别
    sed -i "s/\\(.*\\)iso/test.iso/" vm.xml
    sed -i 's/\(.*\)iso/test.iso/' vm.xml
