http
====

#. 请求信息

   .. code-block:: go

      // 请求方法
      ctx.Method()

      // 
      ctx.RequestURI()

      ctx.Path()

      ctx.Host()

      ctx.QueryArgs()

      ctx.UserAgent()

      // 连接建立时刻
      ctx.ConnTime()

      // 请求开始时刻
      ctx.Time()

      ctx.ConnRequestNum()

      ctx.RemoteIP()

#. 设置 header

   .. code-block:: go

      ctx.Response.Header.Set("X-My-Header", "my-header-value")

#. 设置 cookies

   .. code-block:: go

      var c fasthttp.Cookie
      c.SetKey("cookie-name")
      c.SetValue("cookie-value")
      ctx.Response.Header.SetCookie(&c)