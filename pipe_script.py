pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[credentialsId: '357dddca-e6bd-4287-8446-acc09fe26bac', url: 'https://github.com/Rohan-14-1/Devops_proj.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: '357dddca-e6bd-4287-8446-acc09fe26bac', url: 'https://github.com/Rohan-14-1/Devops_proj.git'
                bat 'python pipe_sort.py'
                
            }
        }
        stage('Test') {
            steps {
                echo "Testing is done"
            }
        }
    }
}
