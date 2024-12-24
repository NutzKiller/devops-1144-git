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
                            set -e  # Fail on errors
                            
                            # Ensure pip installs pytest in the correct directory
                            pip install --user pytest

                            # Update PATH to include the directory where pytest is installed
                            export PATH=$PATH:$HOME/.local/bin

                            # Check if pytest is available in the path
                            command -v pytest

                            # Run tests
                            pytest --junitxml=report.xml
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
                // Optionally log running containers
                sh 'docker ps'
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
