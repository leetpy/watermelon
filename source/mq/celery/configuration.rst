配置
====

从4.0版本开始，celery 使用 小写下划线连接方式命令配置项；



#. 保存 task 执行状态和结果

   配置 *result_backend*, 保存的结果格式如下：

   正常时的消息

   .. code-block:: json

       {
           "status": "SUCCESS",
           "result": 10,
           "traceback": null,
           "children": [],
           "task_id": "20fb6fb0-0ef2-4a2f-9517-2fbb5e41e443",
           "date_done": "2020-09-05T07:40:18.085679"
       }

   异常时的消息

   .. code-block:: json

    {
    	"status": "FAILURE",
    	"result": {
    		"exc_type": "ZeroDivisionError",
    		"exc_message": [
    			"division by zero"
    		],
    		"exc_module": "builtins"
    	},
    	"traceback": "Traceback (most recent call last):\n  File \"/Users/sealee/.pyenv/versions/3.8.1/envs/tianhe/lib/python3.8/site-packages/celery/app/trace.py\", line 385, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"/Users/sealee/.pyenv/versions/3.8.1/envs/tianhe/lib/python3.8/site-packages/celery/app/trace.py\", line 648, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"/Users/sealee/code/mq/consumer.py\", line 13, in add\n    1/ 0\nZeroDivisionError: division by zero\n",
    	"children": [],
    	"task_id": "b7364eda-bbd4-4dc7-89ba-16589dff8401",
    	"date_done": "2020-09-05T08:07:12.214929"
    }

   如果同时在 task 里配置了 *ignore_result=True* , 则不会保存结果到对应的 backend.

#. 消费配置

   通过配置项 *broker_transport_options* 可以配置消费参数；

   .. code-block:: python

    broker_transport_options = {
        'max_retries': 5  #  最大尝试次数
    }

#. 消费完之后再 Acknowledged

   celery 默认 ACK 是当一个任务执行后，立刻发送 Acknowledged 信号，标记该任务已经被执行。
   但是异常中断时，该任务不会被重新分发。可以通过配置 *task_acks_late* 让任务执行完成后再
   发送 Acknowledged. 这样可以保证不丢消息，但最好保证消费是幂等的，不然会影响结果。

#. 读多条消息

   默认情况下，celery worker 一次会读取4条消息，可以通过 *worker_prefetch_multiplier* 配置，
   如果不希望一次读多条，设置为 1， 如果设置为 0， 则 worker 一次会读取尽可能多的消息。