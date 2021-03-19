time
====

计算日期偏移

`AddDate(years int, months int, days int)`


.. code-block:: go

   format := "2006-01-02"

   //  2015-05-01
   d1, _ := time.Parse(format, "2015-03-31")
   fmt.Println(d1.AddDate(0, 2, 0))

   // 2015-05-30
   d2, _ := time.Parse(format, "2015-04-30")
   fmt.Println(d2.AddDate(0, 1, 0))

   // 2013-03-01
   d3, _ := time.Parse(format, "2012-02-29")
   fmt.Println(d3.AddDate(1, 0, 0))