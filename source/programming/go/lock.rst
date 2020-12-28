锁
==


- 互斥锁

  .. code-block:: go

     func main() {
         var mutex sync.Mutex
         count := 0

         for r := 0; r < 50; r++ {
            go func() {
                    mutex.Lock()
                    count += 1
                    mutex.Unlock()
                }()
            }

            time.Sleep(time.Second)
            fmt.Println("the count is : ", count)
         }


- 读写锁

  #. `func (rw *RWMutex) Lock()`
  #. `func (rw *RWMutex) RLock()`
  #. `func (rw *RWMutex) RLocker() Locker`
  #. `func (rw *RWMutex) RUnlock()`
  #. `func (rw *RWMutex) Unlock()`