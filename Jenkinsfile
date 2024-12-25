
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
                    echo "Cleaning up previous workspace..."
                    // Remove any previous clone of the repo
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

                    echo "Repository cloned. Verifying directory structure..."
                    sh 'pwd'  // Confirm current directory
                    sh 'ls -R' // List files recursively to check the repo structure
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
                    echo "Generated version tag: $VERSION"
                }
            }
        }

        stage('Docker Compose Up') {
            steps {
                script {
                    // Navigate to the flask_catgif_clean directory
                    dir('devops-1144-git/flask_catgif_clean') {
                        script {
                            echo "Checking if docker-compose.yaml exists..."
                            if (fileExists('docker-compose.yaml')) {
                                echo "Found docker-compose.yaml, bringing down existing containers"
                                sh '''
                                    docker-compose down
                                    docker-compose pull
                                    echo "Starting Docker Compose"
                                    docker-compose up -d
                                '''
                            } else {
                                error "docker-compose.yaml not found in the directory. Exiting pipeline."
                            }
                        }
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
                        sh '''
                            echo "Building the Flask Docker image"
                            docker-compose build flask_app
                        '''
                        if (VERSION) {
                            sh "docker tag nutzkiller/flask_catgif_clean:latest $IMAGE_NAME:$VERSION"
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
            }
        }
    }
}
