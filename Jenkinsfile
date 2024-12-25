pipeline {
    agent any
    environment {
        DB_HOST = credentials('db_host')
        DB_USER = credentials('db_user')
        DB_PASSWORD = credentials('db_password')
        DB_NAME = credentials('db_name')
        PORT = '5000'
        IMAGE_NAME = 'nutzkiller/flask_catgif_clean'
        VERSION = ''
    }
    stages {
        stage('Cleanup Workspace') {
            steps {
                script {
                    echo "Cleaning up workspace..."
                    sh 'rm -rf devops-1144-git'
                }
            }
        }

        stage('Clone Repository') {
            steps {
                script {
                    echo "Cloning the repository..."
                    checkout([$class: 'GitSCM',
                              branches: [[name: '*/main']],
                              userRemoteConfigs: [[url: 'https://github.com/NutzKiller/devops-1144-git.git']]])
                    echo "Repository cloned successfully."
                }
            }
        }

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
                    VERSION = "1.0.${BUILD_NUMBER}"
                    echo "Using Jenkins build number $VERSION as the image version"
                }
            }
        }

        stage('Docker Compose Down and Up') {
            steps {
                script {
                    echo "Navigating to Flask project directory..."
                    dir('devops-1144-git/flask_catgif_clean') {
                        echo "Bringing down existing containers and starting Docker Compose..."
                        sh '''
                            docker-compose down
                            docker-compose pull
                            docker-compose up -d
                        '''
                    }
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub_credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        echo "Logging into Docker Hub..."
                        sh '''
                            echo $DOCKER_PASSWORD | docker login --username $DOCKER_USERNAME --password-stdin
                        '''
                    }
                }
            }
        }

        stage('Build and Push Flask Image') {
            steps {
                script {
                    echo "Building and pushing the Flask Docker image..."
                    dir('devops-1144-git/flask_catgif_clean') {
                        sh '''
                            docker-compose build flask_app
                            docker tag nutzkiller/flask_catgif_clean:latest $IMAGE_NAME:$VERSION
                            docker push $IMAGE_NAME:$VERSION
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                echo "Cleaning up resources..."
                dir('devops-1144-git/flask_catgif_clean') {
                    sh 'docker-compose down'
                }
            }
        }
    }
}
