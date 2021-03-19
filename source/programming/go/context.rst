context
=======

控制并发的方式


Context 定义

.. code-block:: go

   type Context interface {
       Deadline() (deadline time.Time, ok bool)

       Done() <-chan struct{}

       Err() error

       Value(key interface{}) interface{}
   }


有哪些类型的 Context

- Background
- TODO


context 包常用函数

- func WithCancel(parent Context) (ctx Context, cancel CancelFunc)

WaitGroup