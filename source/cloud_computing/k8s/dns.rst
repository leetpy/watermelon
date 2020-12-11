DNS
===


**CoreDNS 策略**


- None：表示空的DNS设置，这种方式一般用于想要自定义DNS配置的场景，而且，
  往往需要和dnsConfig配合一起使用达到自定义DNS的目的。

- Default：有人说Default的方式，是使用宿主机的方式，这种说法并不准确。
  这种方式其实是让kubelet来决定使用何种DNS策略。而kubelet默认的方式，就是使用宿主机的 /etc/resolv.conf，
  但是kubelet是可以灵活来配置使用什么文件来进行DNS策略的，
  我们完全可以使用kubelet的参数：–resolv-conf=/etc/resolv.conf 来决定您的DNS解析文件地址。

- ClusterFirst：这种方式表示Pod内的DNS使用集群中配置的DNS服务，简单来说，
  就是使用Kubernetes中kubedns或coredns服务进行域名解析。如果解析不成功，才会使用宿主机的DNS配置进行解析。

- ClusterFirstWithHostNet: 优先使用宿主机的DNS配置进行解析


如果未明确指定dnsPolicy，则默认使用 **ClusterFirst**


- 如果将dnsPolicy设置为“Default”，则名称解析配置将从运行pod的工作节点继承。

- 如果将dnsPolicy设置为“ClusterFirst”，则DNS查询将发送到kube-dns服务。
  对于以配置的集群域后缀为根的域的查询将由kube-dns服务应答。所有其他查询（例如，www.kubernetes.io）
  将被转发到从节点继承的上游名称服务器。在此功能之前，通常通过使用自定义解析程序替换上游DNS来引入存根域。
  但是，这导致自定义解析程序本身成为DNS解析的关键路径，其中可伸缩性和可用性问题可能导致群集丢失DNS功能。
  此特性允许用户在不接管整个解析路径的情况下引入自定义解析。

如果某个工作负载不需要使用集群内的coredns，可以使用kubectl命令或API将此策略设置为dnsPolicy: Default。


**配置方式**

.. code-block:: yaml

   apiVersion: apps/v1beta1
   kind: Deployment
   metadata:
     name: nginx
     labels:
       app: nginx
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         labels:
           app: nginx
       spec:
         containers:
           - name: nginx
             image: nginx:latest
         dnsPolicy: ClusterFirstWithHostNet


**options 设置**

.. code-block:: yaml

   dnsConfig:
     options:
       - name: timeout
         value: '2'
       - name: ndots
         value: '5'
       - name: single-request-reopen