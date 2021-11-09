
lua
===

- access_by_lua
- access_by_lua_block
- content_by_lua
- content_by_lua_file


# 设置 header: ngx.req.set_header(header_name, value)
# 清除 header: ngx.req.clear_header(header)

清除所有的 headers_M = {}

.. code-block:: lua

   for header, _ in pairs(ngx.req.get_headers()) do
       ngx.req.clear_header(header)
   end