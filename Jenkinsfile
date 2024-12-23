pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')  // Poll SCM every minute
    }

    stages {
        stage('Cleanup') {
            steps {
                script {
                    // Navigate to the flask_catgif_clean directory and stop/remove containers if they exist
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down || echo "No containers to stop or remove"'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    // Clone the repository and build the Docker images using docker-compose
                    sh 'rm -rf devops-1144-git'
                    sh 'git clone https://github.com/NutzKiller/devops-1144-git.git'
                    
                    // Ensure .env file exists and load the environment variables into the pipeline environment
                    sh '''
                    if [ -f devops-1144-git/flask_catgif_clean/.env ]; then
                        export $(cat devops-1144-git/flask_catgif_clean/.env | xargs)
                    else
                        echo ".env file not found"
                        exit 1
                    fi
                    '''
                    
                    // Pass environment variables explicitly to docker-compose build
                    sh 'cd devops-1144-git/flask_catgif_clean && PORT=$PORT DB_HOST=$DB_HOST DB_USER=$DB_USER DB_PASSWORD=$DB_PASSWORD DB_NAME=$DB_NAME docker-compose build'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Ensure .env file is sourced and variables are passed to docker-compose
                    sh '''
                    if [ -f devops-1144-git/flask_catgif_clean/.env ]; then
                        export $(cat devops-1144-git/flask_catgif_clean/.env | xargs)
                    else
                        echo ".env file not found"
                        exit 1
                    fi
                    '''
                    
                    sh 'cd devops-1144-git/flask_catgif_clean && PORT=$PORT DB_HOST=$DB_HOST DB_USER=$DB_USER DB_PASSWORD=$DB_PASSWORD DB_NAME=$DB_NAME docker-compose up -d'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Wait for the container to start
                    sh 'sleep 5'
                    
                    // Test if the app is running by making a request
                    sh '''
                    if ! curl -f http://localhost:5000; then
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
                    // Navigate to the flask_catgif_clean directory and clean up after the run
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down'
                }
            }
        }
    }
}
