Go module
=========

Go 的依赖管理比较混乱，在 Go 1.11 版本引入了 Go Modules.

启用 go modules
----------------

启用条件：

#. go 版本大于 v1.11
#. 设置 GO111MODULE 环境变量

要使用go module 首先要设置GO111MODULE=on，GO111MODULE 有三个值，
off、on、auto，off 和 on 即关闭和开启，auto 则会根据当前目录下是否有 go.mod 文件来判断是否使用 modules 功能。
无论使用哪种模式，module 功能默认不在 GOPATH 目录下查找依赖文件，所以使用 modules 功能时请设置好代理。

使用
----

.. code-block:: bash

    export GO111MODULE=on

    # 初始化
    go mod init github.com/you/hello

    # go build 会将项目的依赖添加到 go.mod 中
    go build


配置代理
--------

.. code-block:: bash

    export GOPROXY=https://mirrors.aliyun.com/goproxy/