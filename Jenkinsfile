pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')  // Poll SCM every minute
    }

    environment {
        // Use the 'flask_env' secret to inject environment variables
        FLASK_ENV = credentials('flask_env')
    }

    stages {
        stage('Cleanup') {
            steps {
                script {
                    // Stop and remove any existing containers
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down || echo "No containers to stop or remove"'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    // Clone the repository and build Docker images
                    sh 'rm -rf devops-1144-git'
                    sh 'git clone https://github.com/NutzKiller/devops-1144-git.git'

                    // Inject environment variables from the 'flask_env' secret
                    sh '''
                    cd devops-1144-git/flask_catgif_clean
                    echo "PORT=${PORT}" >> .env
                    echo "DB_HOST=${DB_HOST}" >> .env
                    echo "DB_USER=${DB_USER}" >> .env
                    echo "DB_PASSWORD=${DB_PASSWORD}" >> .env
                    echo "DB_NAME=${DB_NAME}" >> .env
                    docker-compose build
                    '''
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Start the containers using Docker Compose
                    sh '''
                    cd devops-1144-git/flask_catgif_clean
                    docker-compose up -d
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Wait for the container to start
                    sh 'sleep 5'
                    
                    // Test if the app is running
                    sh '''
                    if ! curl -f http://localhost:${PORT}; then
                        echo "App is not reachable."
                        docker logs flask_catgif_clean_flask_app
                        exit 1
                    fi
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Cleanup After Run') {
            steps {
                script {
                    // Stop and clean up containers
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down'
                }
            }
        }
    }
}
