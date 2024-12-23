pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')  // Poll SCM every minute
    }

    environment {
        // Inject Jenkins secrets into environment variables
        DB_HOST = credentials('DB_HOST')   // Ensure the secret is named 'DB_HOST' in Jenkins
        DB_USER = credentials('DB_USER')   // Ensure the secret is named 'DB_USER' in Jenkins
        DB_PASSWORD = credentials('DB_PASSWORD')   // Ensure the secret is named 'DB_PASSWORD' in Jenkins
        DB_NAME = credentials('DB_NAME')   // Ensure the secret is named 'DB_NAME' in Jenkins
        PORT = credentials('PORT')         // Ensure the secret is named 'PORT' in Jenkins
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

                    // Build the Docker images using docker-compose
                    sh '''
                    cd devops-1144-git/flask_catgif_clean
                    docker-compose build
                    '''
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Start the containers using Docker Compose with the environment variables
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
