pprof火焰图
===========

pprof 可以用来统计 cpu 和内存的使用情况。如果应用是api或者服务类型的，使用 `net/http/pprof` 库，
如果是单次运行的，使用 `runtime/pprof` 工具。

火焰图依赖 graphviz 工具，安装方式如下：

.. code-block:: bash

    # for macos
    brew install graphviz

    # for unbunt
    apt install graphviz -y

    # for centos
    yum install graphviz -y

.. NOTE::

    go 1.11 开始已经支持火焰图了，如果是之前的版本，可以使用 go-torch.

runtime/pprof
-------------

先看看 `runtime/pprof` 的使用方式，示例代码如下：

.. code-block:: go

    package main

    import (
    	"flag"
    	"log"
    	"os"
    	"runtime"
    	"runtime/pprof"
        "time"
    )
    
    var cpuprofile = flag.String("cpuprofile", "", "write cpu profile to `file`")
    var memprofile = flag.String("memprofile", "", "write memory profile to `file`")
    
    func count() {
    	sum := 0
    	for i := 0; i < 1000000; i++ {
    		sum += i
    		for j := 0; j < 10000; j++ {
    			sum -= j
    		}
    	}
    	fmt.Println(sum)
    }

    func sleep() {
    	a := []string{"a", "b", "c", "d"}
    	for i := range a {
    		fmt.Println(i)
    	}
    	time.Sleep(time.Second * 5)
    }
    func main() {
    	flag.Parse()
    	if *cpuprofile != "" {
    		f, err := os.Create(*cpuprofile)
    		if err != nil {
    			log.Fatal("could not create CPU profile: ", err)
    		}
    		defer f.Close() // error handling omitted for example
    		if err := pprof.StartCPUProfile(f); err != nil {
    			log.Fatal("could not start CPU profile: ", err)
    		}
    		defer pprof.StopCPUProfile()
    	}

    	if *memprofile != "" {
    		f, err := os.Create(*memprofile)
    		if err != nil {
    			log.Fatal("could not create memory profile: ", err)
    		}
    		defer f.Close() // error handling omitted for example
    		runtime.GC()    // get up-to-date statistics
    		if err := pprof.WriteHeapProfile(f); err != nil {
    			log.Fatal("could not write memory profile: ", err)
    		}
    	}

        count()
        sleep()
    }


生成 pprof 文件

.. code-block:: bash

    # 生成二进制文件
    go build main.go

    # 生成 prof 文件
    go run main.go -cpuprofile cpu.prof -memprofile mem.prof

web 查看

.. code-block:: bash

    go tool pprof -http=":8081" main cpu.prof


net/http/pprof
---------------

示例代码：

.. code-block:: go

    package main

    import (
    	"fmt"
    	"log"
    	"net/http"
    	_ "net/http/pprof"
    )

    func main() {
    	go func() {
    		log.Println(http.ListenAndServe(":8080", nil))
    	}()

    	// 占用 cpu
    	for {
    		fmt.Println("hello")
    	}
    }


如果是默认的 `http.DefaultServeMux`, 只需要加一行 import 就行： `_ "net/http/pprof"`,


如果你使用自定义的 Mux，则需要手动注册一些路由规则：

.. code-block:: go

   r.HandleFunc("/debug/pprof/", pprof.Index)
   r.HandleFunc("/debug/pprof/cmdline", pprof.Cmdline)
   r.HandleFunc("/debug/pprof/profile", pprof.Profile)
   r.HandleFunc("/debug/pprof/symbol", pprof.Symbol)
   r.HandleFunc("/debug/pprof/trace", pprof.Trace)

#. 编译 `go build main.go`
#. 运行 server `go run main.go`
#. 访问 `http://localhost:8080/debug/pprof/`
#. 点击 `profile` 会下载随后 30s 的cpu profile 文件;
#. web 查看 go tool pprof -http=":8081" main profile