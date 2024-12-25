pipeline {
    agent any
    environment {
        DB_HOST = credentials('db_host')
        DB_USER = credentials('db_user')
        DB_PASSWORD = credentials('db_password')
        DB_NAME = credentials('db_name')
        PORT = '5000'  // Non-sensitive, so we define it directly
        IMAGE_NAME = 'nutzkiller/flask_catgit_clean'  // Docker Hub image name
        VERSION = ''  // This will store the version tag
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

        stage('Generate Version Tag') {
            steps {
                script {
                    // Generate the version tag using the Git commit hash or fallback to 'latest'
                    VERSION = sh(script: 'git rev-parse --short HEAD || echo "latest"', returnStdout: true).trim()
                    echo "Using Git commit hash $VERSION as image version"
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
                            docker-compose pull
                            echo "Starting Docker Compose"
                            docker-compose up -d
                        '''
                    }
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Use Jenkins Docker Hub credentials to log in
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
                        // Build the Docker image using docker-compose
                        sh '''
                            echo "Building the Flask Docker image"
                            docker-compose build flask_app
                        '''
                        // Only tag and push if VERSION is not empty
                        if (VERSION) {
                            echo "Tagging the Docker image"
                            // Tag the image based on the service defined in the compose file
                            sh "docker tag nutzkiller/flask_catgif_clean:latest $IMAGE_NAME:$VERSION"
                            echo "Pushing the image to Docker Hub"
                            sh "docker push $IMAGE_NAME:$VERSION"
                        } else {
                            echo "VERSION is empty. Skipping push."
                        }
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
    }
}
