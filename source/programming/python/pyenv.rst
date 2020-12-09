pyenv
=====

pyenv可以帮助你在一台开发机上建立多个版本的python环境， 并提供方便的切换方法。
virtualenv可以搭建虚拟且独立的python环境，可以使每个项目环境与其他项目独立开来，
保持环境的干净，解决包冲突问题。

安装
----

.. code-block:: bash

   git clone https://github.com/pyenv/pyenv.git ~/.pyenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
   echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

   # restart shell
   exec "$SHELL"

安装 python 版本
-----------------

.. code-block:: bash

   # 安装 python 版本
   pyenv install 2.7.10

   # centos 需要安装如下包
   yum install patch openssl-devel -y


pyenv-virtualenv 安装
------------------------

光有pyenv还不够，我们需要结合virtualenv来使用, pyenv-virtualenv就是干这个活的。

.. code-block:: bash

   git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

   # restart shell
   exec "$SHELL"


使用
----

.. code-block:: bash

   # 查看支持哪些版本
   pyenv install -l

   # 创建项目
   pyenv virtualenv 2.7.10 project

   # Activate virtualenv
   pyenv activate project

   # Deactive virtualenv
   pyenv deactivate

   # Delete existing virtualenv
   pyenv uninstall project

   # 查看已经安装了哪些 virtualenv
   pyenv versions


FAQ
===

- `/root/.pyenv/plugins/python-build/bin/python-build: line 1326: patch: command not found`

  .. code-block:: bash

     yum install patch -y

- mac os zlib 问题

  现象如下：

  .. code-block:: console

     Last 10 log lines:
     File "/private/var/folders/qq/cxqjcr296h7bvhl4nqbzrsn00000gn/T/python-build.20190419143439.41015/Python-3.5.3/Lib/ensurepip/__main__.py", line 4, in <module>
       ensurepip._main()
     File "/private/var/folders/qq/cxqjcr296h7bvhl4nqbzrsn00000gn/T/python-build.20190419143439.41015/Python-3.5.3/Lib/ensurepip/__init__.py", line 209, in _main
       default_pip=args.default_pip,
     File "/private/var/folders/qq/cxqjcr296h7bvhl4nqbzrsn00000gn/T/python-build.20190419143439.41015/Python-3.5.3/Lib/ensurepip/__init__.py", line 116, in bootstrap
       _run_pip(args + [p[0] for p in _PROJECTS], additional_paths)
     File "/private/var/folders/qq/cxqjcr296h7bvhl4nqbzrsn00000gn/T/python-build.20190419143439.41015/Python-3.5.3/Lib/ensurepip/__init__.py", line 40, in _run_pip
       import pip
     zipimport.ZipImportError: can't decompress data; zlib not available

  解决办法：

  .. code-block:: bash

     brew install zlib
     export LDFLAGS="-L/usr/local/opt/zlib/lib"
     export CPPFLAGS="-I/usr/local/opt/zlib/include"
     export PKG_CONFIG_PATH="/usr/local/opt/zlib/lib/pkgconfig"