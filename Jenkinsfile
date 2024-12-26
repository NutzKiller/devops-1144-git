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
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Clone Repository') {
            steps {
                script {
                    checkout([$class: 'GitSCM', 
                        branches: [[name: '*/main']], 
                        userRemoteConfigs: [[
                            url: 'https://github.com/your-repo/devops-1144-git.git', 
                            credentialsId: 'Github-cred'
                        ]]
                    ])
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
                    VERSION = "${BUILD_NUMBER}"
                    echo "Using Jenkins build number $VERSION as the image version"
                }
            }
        }

        stage('Docker Compose Up') {
            steps {
                script {
                    dir('flask_catgif_clean') {
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
                    dir('flask_catgif_clean') {
                        sh '''
                            echo "Building the Flask Docker image"
                            docker-compose build flask_app
                        '''
                        if (VERSION) {
                            sh "docker tag $IMAGE_NAME:latest $IMAGE_NAME:$VERSION"
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
