pipeline {
    agent any 

    stages {
        stage('Build') {
            agent any 
            steps {
                sh 'docker-compose up -d --build'
            }
        }

        stage('Test') {
            agent any
            steps {
                sh 'docker-compose exec -T proxy pytest /proxy/tests/end2end/limit_requests.py'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
        }
    }
}
