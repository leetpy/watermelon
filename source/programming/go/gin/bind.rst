参数绑定
========


#. 参数校验

   .. code-block:: go

      // require
      type UserParams struct {
          Name     string `json:"name" binding:"required"`
          Password string `json:"password" binding:"required"`
      }