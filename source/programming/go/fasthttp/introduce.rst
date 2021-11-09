介绍
====

项目地址： https://github.com/valyala/fasthttp

fasthttp 不仅是server 端，也可以当 client 使用。

安装：

.. code-block:: bash

   go get -u github.com/valyala/fasthttp

最佳实践
--------

- 不要分配 `[]byte` 缓冲区，尽可能的复用；
- 多使用 `sync.Pool`；