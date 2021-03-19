Pipeline
=========

- 触发其它 job

  .. code-block:: groovy

      stage("step1") {
          steps {
              build job: 'aether-cleaner-update', parameters: []
          }
      }

- 指定分支和文件改变条件

  .. code-block:: groovy

     stage("step1") {
         when{
             environment name: 'GIT_BRANCH', value: 'origin/test'
             anyOf {
                 changeset 'go.mod'
                 changeset 'go.sum'
                 changeset 'docker/Dockerfile'
             }
     }

- 失败发送邮件

  .. code-block:: groovy

     pipeline {
         post {
             failure {
                 emailext(
                     subject: "Jenkins build is ${currentBuild.result}: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                     mimeType: "text/html",
                     body: """<p>Jenkins build is ${currentBuild.result}: ${env.JOB_NAME} #${env.BUILD_NUMBER}:</p>
                              <p>Check console output at <a href="${env.BUILD_URL}console">${env.JOB_NAME} #${env.BUILD_NUMBER}</a></p>""",
                     recipientProviders: [[$class: 'CulpritsRecipientProvider'],
                                         [$class: 'DevelopersRecipientProvider'],
                                         [$class: 'RequesterRecipientProvider']]
                 )
             }
         }
     }

- 控制 job 每次只有一个在运行

  .. code-block:: groovy

     pipeline {
         options {
             disableConcurrentBuilds()
         }
     }

- 构建参数

  .. code-block:: groovy

     pipeline {
         agent any
         parameters {
     	     string(name: 'IMG_NAME', defaultValue: 'default value', description: 'parameters description')
     	 }

         stages {
             stage("parameters test") {
                 steps {
                     sh """
                         echo "${params.IMG_NAME}"
                     """
                     }
                 }
             }
         }
     }