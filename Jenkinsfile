def gv
pipeline {
    agent {
        label 'ram'
    }
    parameters {
        choice(name: 'VERSION', choices: ['1.1.0','1.2.0','1.3.0'], description: '')
        booleanParam(name: 'excuteTests', defaultValue: true,description: '')
    }
    stages {
         stage('init'){
            steps{
                script {
                    gv = load "script.groovy"
                }
            }
        }
        stage('built') {
            steps {
                script {
                 gv.buldApp()   
                }
            }  
        }
        stage('test') {
             when {
                 expression {
                     params.excuteTests
                 }
             }
            steps {
                script {
                    gv.testApp()
                }
        }
    }
         stage('deploye') {
            steps {
                script {
            gv.deployApp()   
                }
        }
    }
  }
}
