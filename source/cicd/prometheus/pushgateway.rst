Pushgateway
===========

正常情况下，prometheus 是拉模式，prometheus server 从各个数据源拉取 metrics 信息。
pushgateway 是我们将数据主动 push 到 Pushgateway，然后 prometheus 从 pushgateway
拉取数据。