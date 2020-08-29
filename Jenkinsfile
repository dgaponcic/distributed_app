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
            sh 'docker-compose push'
            sh 'docker-compose down'
            // ToDo write docker compose on rpi
            // ToDo execute "docker stack deploy --compose-file docker-compose.yaml distributed_app" on rpi
        }
    }
}
