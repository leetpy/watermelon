task
====


调用异步任务的方式，用下例子说明：

.. code-block:: python

   @app.task
   def add(x, y):
       return x + y

- task.delay()

  适合简单的 task 调用，eg:

  .. code-block:: python

     add.delay(1, 2)

- task.apply_async()

  可以加控制参数

- app.send_task()