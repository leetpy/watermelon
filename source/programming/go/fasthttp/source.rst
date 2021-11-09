源码分析
========

.. code-block:: go

   // 这里的 handler 是一个函数
   func ListenAndServe(addr string, handler RequestHandler) error {}

   type RequestHandler func(ctx *RequestCtx)