pipeline {
    agent {
        label 'ram'
    }
    parameters {
        choice(name: 'VERSION', choices: ['1.1.0','1.2.0','1.3.0'], description: '')
        booleanParam(name: 'excuteTests', defaultValue: true,description: '')
    }
    stages {
        stage('built') {
            steps {
                echo 'build the application'
                echo "build with mentioned version "
            }  
        }
        stage('test') {
             when {
                 expression {
                     params.excuteTests
                 }
             }
            steps {
                echo 'test the application'
        }
    }
         stage('deploye') {
            steps {
                echo 'deploye the the application on server'
                echo "doploy the version ${VERSION}"
        }
    }
  }
}
