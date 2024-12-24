pipeline {
    agent any
    environment {
        DB_HOST = credentials('db_host')
        DB_USER = credentials('db_user')
        DB_PASSWORD = credentials('db_password')
        DB_NAME = credentials('db_name')
        PORT = '5000'  // Non-sensitive, so we define it directly
        IMAGE_NAME = 'nutzkiller/flask_catgif_clean'  // Docker Hub image name
        VERSION = ''  // Will be determined dynamically
    }
    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    echo "Using the following database configurations:"
                    echo "DB_HOST: [hidden]"
                    echo "DB_USER: [hidden]"
                    echo "DB_NAME: [hidden]"
                    echo "PORT: $PORT"
                }
            }
        }

        stage('Set Version') {
            steps {
                script {
                    // If VERSION is not set, generate a new version
                    if (VERSION == '') {
                        // Example: Generate a version based on the current date (YYYY.MM.DD)
                        def date = new Date()
                        VERSION = "${date.format('yyyy.MM.dd')}"
                        echo "Generated new version: $VERSION"
                    } else {
                        echo "Using existing version: $VERSION"
                    }
                }
            }
        }

        stage('Docker Compose Up') {
            steps {
                script {
                    dir('devops-1144-git/flask_catgif_clean') {
                        sh '''
                            echo "Bringing down existing containers"
                            docker-compose down --volumes  # Ensuring cleanup of containers and volumes
                            docker-compose pull
                            echo "Starting Docker Compose"
                            docker-compose up -d
                            # Running logs in the background so the pipeline doesn't get stuck
                            docker-compose logs -f &  
                        '''
                    }
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub_credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                            echo "Logging into Docker Hub"
                            echo $DOCKER_PASSWORD | docker login --username $DOCKER_USERNAME --password-stdin
                        '''
                    }
                }
            }
        }

        stage('Build and Push Flask Image') {
            steps {
                script {
                    dir('devops-1144-git/flask_catgif_clean') {
                        // Build the Flask app Docker image
                        sh '''
                            echo "Building the Flask Docker image"
                            docker-compose build flask_app
                        '''
                        
                        // Tag the built image with both latest and the new version
                        sh '''
                            echo "Tagging the Docker image"
                            if [ -z "$VERSION" ]; then echo "Error: VERSION is not set!"; exit 1; fi
                            docker tag flask_catgif_clean_flask_app:latest $IMAGE_NAME:$VERSION
                            docker tag flask_catgif_clean_flask_app:latest $IMAGE_NAME:latest
                        '''
                        
                        // Push the Docker image to Docker Hub
                        sh '''
                            echo "Pushing the image to Docker Hub"
                            docker push $IMAGE_NAME:$VERSION
                            docker push $IMAGE_NAME:latest
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
                // Stop and remove the containers if needed
                sh 'docker-compose down --volumes'  // Cleanup containers and volumes
                sh 'docker system prune -f'  // Optional cleanup of unused images and stopped containers
            }
        }
    }
}
