json 处理
==========

.. warning::
    如果序列化成JSON，只有大写开头的变量才会被序列化。

eg: 下面的例子中，age 字段不会被序列化。

.. code-block:: go

    type Student struct {
        Name string `json:"name"`
        age  int    `json:"age"`
    }

#. 针对可有可无的字段

   如果有些字段不一定存在，可以使用 *omitempty*  注解，但是不能区分零值和是否存在, eg:

   .. code-block:: go

       type Domain struct {
           Hosts  []string `json:"hosts"`
           TaskID string   `json:"task_id,omitempty"`
       }