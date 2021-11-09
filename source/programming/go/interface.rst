interface
=========

interface 定义

特点：

#. 函数没有 {}
#. 函数有参数和返回值

.. code-block:: go

   type Writer interface {
       Write(p []byte) (n int, err error)
   }