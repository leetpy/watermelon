基本用法
========

#. 写数据

   .. code-block:: go

      // string
      func (c *Context) String(code int, format string, values ...interface{})

      // json
      func (c *Context) JSON(code int, obj interface{})