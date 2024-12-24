pipeline {
    agent any
    environment {
        DB_HOST = 'db'                      // Non-sensitive, set directly
        DB_USER = 'root'                    // Non-sensitive, set directly
        DB_PASSWORD = credentials('db_password') // Use Jenkins credentials for sensitive data
        DB_NAME = 'catgifs'                 // Non-sensitive, set directly
        PORT = '5000'                       // Non-sensitive, set directly
    }
    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    echo "DB_HOST: $DB_HOST"
                    echo "DB_USER: $DB_USER"
                    echo "DB_NAME: $DB_NAME"
                    echo "PORT: $PORT"
                    // Do not print sensitive data like DB_PASSWORD
                }
            }
        }
        stage('Docker Compose Up') {
            steps {
                script {
                    dir('devops-1144-git/flask_catgif_clean') {
                        sh '''
                            echo "Bringing down existing containers"
                            docker-compose down
                            echo "Starting Docker Compose"
                            docker-compose up -d
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                node {
                    echo "Cleaning up resources"
                    dir('devops-1144-git/flask_catgif_clean') {
                        sh 'docker-compose down'
                    }
                }
            }
        }
    }
}
