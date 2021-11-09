筛选器
======

#. 常见筛选器

   .. code-block:: bash

      # 待我确认关闭
      project = XXX AND issuetype = Bug AND reporter = currentUser() AND status in ("Check", Fixed) ORDER BY created DESC

      # 我汇报的所有问题（处理中）
      project = XXX AND issuetype = Bug AND reporter = currentUser() AND statusCategory = "In Progress" ORDER BY created DESC

      # 所有分配给我的问题（处理中）
      project = XXX AND issuetype = Bug AND assignee = currentUser() AND statusCategory = "In Progress" ORDER BY created DESC

      # 所有未完成BUG
      project = XXX AND issuetype = Bug AND statusCategory = "In Progress" ORDER BY created DESC
