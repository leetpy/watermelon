类型
====

#. 类型断言

   .. code-block:: go

      // 其中i为interface{}类型 T是要断言的类型。
      // 1. 如果 i 是 T 类型，赋值 i 给 t;
      // 2. 如果 i 不是 T 类型，触发 panic
      t := i.(T)

      // 1. 如果 i  是 T 类型，赋值 i 给 T, ok 为 true;
      // 2. 如果 i 不是 T 类型，赋值 T 类型的零值给 i, ok 为 false;
      t, ok := i.(T)

#. 获取变量类型

   .. code-block:: go

      // 获取变量类型
      v1 := "hello"
      // 输出 string, 返回的是 Type 类型
      fmt.Println(reflect.typeOf(v1))

      // 直接打印类型
      fmt.Printf("v1 type:%T\n", v1)

#. 类型转换

   .. code-block:: go

      // string to int
      int, err := strconf.Atoi(string)

      // string to int64
      int64, err := strconv.ParseInt(string, 10, 64)

      // int to string
      string := strconv.Itoa(int)

      // int64 to string
      string := strconv.FormatInt(int64, 10)