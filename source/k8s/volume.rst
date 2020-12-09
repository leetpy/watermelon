Volume
======


- EmptyDir

  两个容器使用同一个 EmptyDir

  .. code-block:: yaml

     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: nginx
     spec:
       selector:
         matchLabels:
           app: nginx
       replicas: 1
       template:
         metadata:
           labels:
             app: nginx
         spec:
           containers:
           - name: api
             image: nginx:latest
             imagePullPolicy: Always
             ports:
             - containerPort: 80
             volumeMounts:
             - name: log-data
               mountPath: /var/log/nginx

           - name: filebeat
             image: filebeat:latest
             imagePullPolicy: Always
             volumeMounts:
             - name: log-data
               mountPath: /var/log/nginx

           volumes:
           - name: log-data
             emptyDir: {}
