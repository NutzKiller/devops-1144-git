pipeline {
    agent any
    environment {
        DB_HOST = credentials('db_host')         // Jenkins secret for DB host
        DB_USER = credentials('db_user')         // Jenkins secret for DB user
        DB_PASSWORD = credentials('db_password') // Jenkins secret for DB password
        DB_NAME = credentials('db_name')         // Jenkins secret for DB name
        PORT = '5000'                            // Default port (if required)
    }
    stages {
        stage('Docker Compose Up') {
            steps {
                dir('devops-1144-git/flask_catgif_clean') {
                    echo "Starting Docker Compose"
                    sh '''
                        # Bring down any existing containers
                        docker-compose down
                        
                        # Bring up the Docker containers
                        docker-compose up -d
                    '''
                }
            }
        }
        stage('Health Check') {
            steps {
                echo "Performing Health Check"
                sh '''
                    curl -f http://localhost:$PORT || exit 1
                '''
            }
        }
    }
    post {
        always {
            echo "Cleaning up resources"
            dir('devops-1144-git/flask_catgif_clean') {
                sh '''
                    docker-compose down
                '''
            }
        }
    }
}
