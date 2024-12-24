pipeline {
    agent any
    environment {
        // Load secrets from Jenkins
        DB_HOST = credentials('flask_env')['DB_HOST']
        DB_USER = credentials('flask_env')['DB_USER']
        DB_PASSWORD = credentials('flask_env')['DB_PASSWORD']
        DB_NAME = credentials('flask_env')['DB_NAME']
        PORT = credentials('flask_env')['PORT']
    }
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage('Cleanup Old Repo') {
            steps {
                echo "Removing old repo if it exists"
                sh 'rm -rf devops-1144-git'
            }
        }
        stage('Checkout Repo') {
            steps {
                echo "Cloning repository"
                sh 'git clone https://github.com/nutzkiller/devops-1144-git.git'
            }
        }
        stage('Docker Compose Up') {
            steps {
                dir('devops-1144-git/flask_catgif_clean') {
                    echo "Starting Docker Compose"
                    sh '''
                        docker-compose down
                        DB_HOST=${DB_HOST} DB_USER=${DB_USER} DB_PASSWORD=${DB_PASSWORD} \
                        DB_NAME=${DB_NAME} PORT=${PORT} docker-compose up -d
                    '''
                }
            }
        }
        stage('Health Check') {
            steps {
                script {
                    def response = sh(script: "curl -f http://localhost:${PORT}", returnStatus: true)
                    if (response != 0) {
                        error "Health check failed! Flask app is not reachable."
                    } else {
                        echo "Health check passed! Flask app is running."
                    }
                }
            }
        }
    }
    post {
        always {
            echo "Cleanup resources"
            dir('devops-1144-git/flask_catgif_clean') {
                sh 'docker-compose down'
            }
        }
    }
}
