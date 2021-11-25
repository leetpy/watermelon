协程
====

协程同步
--------

#. sync.WaitGroup

   sync.WaitGroup 只有三个方法， `Add()` 添加计数，`Done()` 计数减一,
   `Wait()` 阻塞，直到计数为0。

   .. code-block:: go

      var wg sync.WaitGroup

      func task(i int) {
          defer wg.Done()
          fmt.Println(i)
      }

      func main() {
          for i := 0; i < 10; i++ {
              wg.Add(1)
              go task(i)
          }

          wg.Wait()
      }

#. 有缓存 channel

   有缓存 channel 不能保证 goroutine 的有序执行。

   .. code-block:: go

      var ch = make(chan int, 10)

      func task(i int) {
          fmt.Println(i)
          time.Sleep(time.Second)
          <- ch
      }

      func main() {
          for i := 0; i < 10; i++ {
              go task(i)
              ch <- i
          }
      }

#. 无缓存 channel

   无缓存 channel 可以保证 goroutine 的有序执行。

   .. code-block:: go

      var ch = make(chan int)

      func task(i int) {
          fmt.Println(i)
          time.Sleep(time.Second)
          <- ch
      }

      func main() {
          for i := 0; i < 10; i++ {
              go task(i)
              ch <- i
          }
      }