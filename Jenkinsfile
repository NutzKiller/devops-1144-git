pipeline {
    agent any
    environment {
        DB_HOST = credentials('db_host')
        DB_USER = credentials('db_user')
        DB_PASSWORD = credentials('db_password')
        DB_NAME = credentials('db_name')
        PORT = '5000' // Non-sensitive, so we define it directly
    }
    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    echo "Using the following database configurations:"
                    echo "DB_HOST: $DB_HOST"
                    echo "DB_USER: $DB_USER"
                    echo "DB_NAME: $DB_NAME"
                    echo "PORT: $PORT"
                    // Do NOT echo sensitive credentials like DB_PASSWORD
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
                echo "Cleaning up resources"
                dir('devops-1144-git/flask_catgif_clean') {
                    sh 'docker-compose down'
                }
            }
        }
    }
}
