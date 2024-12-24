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
                    
                    // Create a virtual environment and install dependencies
                    sh '''
                        echo "Creating virtual environment"
                        python3 -m venv venv
                        source venv/bin/activate
                        echo "Installing dependencies"
                        pip install -r devops-1144-git/flask_catgif_clean/requirements.txt
                    '''
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

        stage('Run Tests') {
            steps {
                script {
                    dir('devops-1144-git/flask_catgif_clean') {
                        sh '''
                            echo "Running tests"
                            source venv/bin/activate
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
                // Keep containers running, don't shut them down
                // You can add docker ps here to verify
            }
        }
    }
}
