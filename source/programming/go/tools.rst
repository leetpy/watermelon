工具使用
========


标准库文档
----------

https://studygolang.com/pkgdoc



pkg.go.dev
-----------

*pkg.go.dev* 是有关Go软件包和模块的信息资源中心。以前看包的文档需要在 godoc.org 上看，
现在pkg.go.dev也提供Go文档功能。并且它懂go module，提供相关软件包以前版本的信息！

.. WARNING::

   如果一个git 库里有多个子项目，路径需要精确到子项目，否则看不到 api Doc!

   eg: github.com/prometheus/client_golang 有 api 和 prometheus， 如果要查看prometheus，
   需要搜索：github.com/prometheus/client_golang/prometheus