不喜欢go的点
============

1. 不允许存在未使用的变量和包；

   这一点有点烦，特别是在代码开发调试阶段，虽然可以通过注释来规避，但总是看着不太爽。
   另外go 的这个检查并不是非常准确。

   eg:
   下面的代码定义了findOptions 变量，实际并没有使用，编译阶段也不会报错。

   .. code-block:: go

      findOptions := options.Find()
      findOptions.SetLimit(2)
      cur, err := collection.Find(context.TODO(), bson.D{})

2. interface 设计：

   如果返回的是一个 interface, 想看具体实现代码时比较麻烦；