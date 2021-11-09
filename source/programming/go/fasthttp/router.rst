router
======

fasthttp 没有没有提供 router, 也没打算集成进来，官方推荐使用第三方路由。这里我们用
`fasthttp-routing`。

#. 基本用法

   .. code-block:: go

      router := routing.New()
      fasthttp.ListenAndServe(":8080", router.HandleRequest)

#. Route Groups

   .. code-block:: go

      router := routing.New()
      api := router.Group("/api")
      api.Use(m1, m2)
      api.Get("/users", h1).Post(h2)
      api.Put("/users/<id>", h3).Delete(h4)

#. router 数据结构

   .. code-block:: go

      type Router struct {
     	  RouteGroup
     	  pool             sync.Pool
    	  routes           map[string]*Route
     	  stores           map[string]routeStore
    	  maxParams        int
    	  notFound         []Handler
    	  notFoundHandlers []Handler
      }

      type RouteGroup struct {
          prefix   string
          router   *Router
          handlers []Handler
      }