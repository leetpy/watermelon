http
====

使用 http.Client
------------------

#. GET

   .. code-block:: go

      package main

      import (
        "io/ioutil"
        "net/http"
        "time"
      )

      func Get(url string) string{
          client := &http.Client{}
          resp, err := client.Get(url)
          if err != nil {
              panic(err)
          }

          // 读取 body
          defer resp.Body.Close()
          body, err := ioutil.ReadAll(resp.Body)
      }


常用操作
--------

#. 设置超时时间

   .. code-block:: go

      // 设置 5s 超时时间
      client := &http.Client{Timeout: 5*time.Second}

#. 设置 header

   .. code-block:: go

      // 需要使用 http.NewRequest
      client := &http.Client{}
      req, err := http.NewRequest("POST", url, bytes.NewReader(jsonStr))
      req.Header.Add("Content-Type", "application/json")
      resp, err := client.Do(req)