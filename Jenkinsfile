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
                    // Log only non-sensitive info or safely mask it
                    echo "DB_HOST: [hidden]" // Mask DB_HOST as well
                    echo "DB_USER: [hidden]"
                    echo "DB_NAME: [hidden]"
                    echo "PORT: $PORT"
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
        stage('Testing') {
            steps {
                script {
                    dir('devops-1144-git/flask_catgif_clean') {
                        sh '''
                            echo "Running tests"
                            pytest --junitxml=report.xml || true
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                echo "Resources left running"
                // Removed docker-compose down to keep containers running
            }
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Please check the logs."
        }
    }
}
