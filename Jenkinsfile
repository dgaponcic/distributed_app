pipeline {
    agent any 

    stages {
        stage('Build Assets') {
            agent any 
            steps {
                sh 'docker-compose up -d --build'
            }
        }

        stage('Test') {
            agent any
            steps {
                sh 'pytest unit_tests/*'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
        }
    }
}
