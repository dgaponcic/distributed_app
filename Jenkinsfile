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
                sh 'docker exec distributed_app_proxy_1 pytest proxy/tests/end2end/limit_requests.py '
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
        }
    }
}
