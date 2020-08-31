pipeline {
    agent any 

    stages {
        stage('Build') {
            agent any 
            steps {
                sh 'echo ${REMOTE_HOST}'
                sh 'docker-compose up -d --build'
            }
        }

        stage('Test') {
            agent any
            steps {
                sh 'docker-compose exec -T proxy pytest /proxy/tests/end2end/limit_requests.py'
            }
        }

        stage('Deploy') {
            agent any
            steps {
                sh 'docker-compose push'
                sh 'scp docker-compose.yaml ${REMOTE_HOST}:distributed/docker-compose.yaml'
                sh 'ssh ${REMOTE_HOST} docker stack deploy --compose-file docker-compose.yaml distributed_app'
            }
        }
    }
    
    post {
        always {
            
            sh 'docker-compose down'
            // ToDo write docker compose on rpi
            // ToDo execute "docker stack deploy --compose-file docker-compose.yaml distributed_app" on rpi
        }
    }
}
