slice
=====

数组和切片是两种不同的数据类型。数组的长度是固定且不可修改的。

数组
----

.. code-block:: go

   // 声明，数组声明时，会用零值初始化
   var arr [5]int

   // 创建并初始化
   arr1 := [5]int{1, 2, 3, 4, 5}

   // 创建并初始化(自动根据给定值计算数组大小)
   arr2 := [...]int{1, 2, 3, 4, 5}

   // 指定部分初始化值
   // [0, 10, 20, 0, 0]
   arr3 := [5]int{1: 10, 2:20}

   // 指针数组
   var arr4 [5]*int
   *arr4[0] = 10

   // 指针数组初始化
   arr4 := [5]*int{0: new(int), 1:new(int)}

   // 下标方式遍历
   for i := 0; i < len(arr); i++ {
   }

   // range 方式遍历
   for idx, value := range arr {
   }

   // 二维数组声明
   var arr5 [4][2]int

易错点
""""""

#. 数组赋值

   .. code-block:: go

      var arr1 [5]int
      arr2 := [5]int{1, 2, 3, 4, 5}

      // 这里 arr1 和 arr2 必须是相同类型
      // 此时只是把 arr2 的内容复制给 arr1，两个数组都是独立的，并不是把 arr1 指向 arr2
      arr1 = arr2

      // 如果是指针数组，则执行的内容是一样的
      var a [2]*int
      b := [2]*int{0: new(int), 1: new(int)}
      a = b
      *a[0] = 3
      // 这里 a[0] 和 b[0] 的地址是相同的
      fmt.Println(a[0], b[0])

#. 函数参数

   .. code-block:: go

      var arr [5]int

      // 数组作为函数参数是传值，而不是传引用，这一点和 python 有很大区别
      func foo1(arr [5]int) {}
      foo1(arr)

      // 通过引用的方式传参
      func foo2(arr *[5]int) {}
      foo2(&arr)

切片
----

#. 切片的内存也是连续的，可以使用索引访问；