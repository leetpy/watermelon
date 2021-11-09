Pipeline
=========

完整的文档参考： https://www.jenkins.io/zh/doc/

- 触发其它 job

  .. code-block:: groovy

     // 等待
     stage("step1") {
        steps {
             build job: 'job1', parameters: []
         }
     }

    // 加参数，不等待
    stage("step1") {
          steps {
              build job: 'job1', parameters: [string(name: 'Name', value: 'Baz2')], wait: false
          }
     }

     // 串行触发多个 job
     stage("step1") {
          steps {
              build job: 'job1', parameters: []
              build job: 'job2', parameters: []
          }
     }

     // 并行触发多个 job，并等待完成
     stage('step1') {
        def jobs = [:]
        jobs[0] = {build job: 'job1', parameters: [string(name: 'Name', value: param)], quietPeriod: 2}
        jobs[1] = {build job: 'job2', parameters: [string(name: 'Name', value: param)], quietPeriod: 2}
        parallel jobs
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
             string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
             text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')
             booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')
             choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')
             password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
     	 }

         stages {
             stage("parameters test") {
                 steps {
                     sh """
                         echo "${params.PERSON}"
                     """
                     }
                 }
             }
         }
     }

- 指定 agent

  .. code-block:: groovy

     // 指定所有 agent
     pipeline {
        agent any
     }

     // 固定 agent
     pipeline {
        agent {
            label "slave"
        }
     }

- stage 失败了继续执行

  .. code-block:: groovy

     pipeline {
        agent any
        stages {
            stage('1') {
                steps {
                    sh 'exit 0'
                }
            }
            stage('2') {
                steps {
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        sh "exit 1"
                    }
                }
            }
            stage('3') {
                steps {
                    sh 'exit 0'
                }
            }
        }
     }

- 按条件触发

  .. code-block:: groovy

     // 根据分支和文件修改来控制
     stage("step1") {
         when {
             anyOf {
                 environment name: 'GIT_BRANCH', value: 'origin/master'
                 changeset 'file_a'
                 changeset 'file_b'
             }
         }
     }

- 发布单元测试结果

  .. code-block:: groovy

     // 这里使用的是 html publish 插件
     // 需要在 jenkins 上执行下： System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
     // 否则 chrome 浏览器会禁用 css 和 js
     post {
         always {
             publishHTML (target : [allowMissing: false,
                 alwaysLinkToLastBuild: true,
                 keepAll: true,
                 reportDir: 'htmlcov',
                 reportFiles: 'index.html',
                 reportName: 'Code Coverage',
                 reportTitles: 'Code Coverage'])
         }
     }