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

        stage('Deploy') {
            agent any
            steps {
                sh 'docker-compose push'
                sh 'scp docker-compose.yaml dianadont@192.168.0.125:distributed/docker-compose.yaml'
                sh 'ssh dianadont@192.168.0.125 docker stack deploy --compose-file docker-compose.yaml distributed_app'
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
