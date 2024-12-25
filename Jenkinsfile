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
                    echo 'Cleaning up workspace...'
                    // Clean up everything in the workspace before cloning
                    sh 'rm -rf *'
                }
            }
        }

        stage('Clone Repository') {
            steps {
                script {
                    echo 'Cloning the repository...'
                    checkout([$class: 'GitSCM',
                              branches: [[name: '*/main']],
                              userRemoteConfigs: [[url: 'https://github.com/NutzKiller/devops-1144-git.git']]])
                }
            }
        }

        stage('Verify Docker Compose File') {
            steps {
                script {
                    echo 'Verifying the presence of docker-compose.yml...'
                    sh '''
                        if [ ! -f devops-1144-git/flask_catgif_clean/docker-compose.yml ] && [ ! -f devops-1144-git/flask_catgif_clean/docker-compose.yaml ]; then
                            echo "No docker-compose.yml or docker-compose.yaml file found in devops-1144-git/flask_catgif_clean"
                            exit 1
                        else
                            echo "docker-compose file found."
                        fi
                    '''
                }
            }
        }

        stage('List Directory Contents') {
            steps {
                script {
                    echo 'Listing directory contents...'
                    sh 'ls -R'
                }
            }
        }

        stage('Prepare Environment') {
            steps {
                script {
                    echo 'Using the following database configurations:'
                    echo 'DB_HOST: [hidden]'
                    echo 'DB_USER: [hidden]'
                    echo 'DB_NAME: [hidden]'
                    echo "PORT: ${PORT}"
                }
            }
        }

        stage('Generate Version Tag') {
            steps {
                script {
                    VERSION = "1.0.${BUILD_NUMBER}"
                    echo "Generated version tag: ${VERSION}"
                }
            }
        }

        stage('Docker Compose Up') {
            steps {
                script {
                    echo 'Changing to directory: devops-1144-git/flask_catgif_clean'
                    dir('devops-1144-git/flask_catgif_clean') {
                        sh '''
                            echo "Current directory: $(pwd)"
                            echo "Listing files in current directory:"
                            ls -l

                            echo "Running Docker Compose commands..."
                            # Check for both docker-compose.yml and docker-compose.yaml
                            if [ -f docker-compose.yml ]; then
                                COMPOSE_FILE=docker-compose.yml
                            elif [ -f docker-compose.yaml ]; then
                                COMPOSE_FILE=docker-compose.yaml
                            fi

                            docker-compose -f $COMPOSE_FILE down || echo "No containers to stop"
                            docker-compose -f $COMPOSE_FILE pull
                            docker-compose -f $COMPOSE_FILE up -d
                        '''
                    }
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub_credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        echo 'Logging into Docker Hub...'
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
                    dir('devops-1144-git/flask_catgif_clean') {
                        echo 'Building and pushing the Flask Docker image...'
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
                echo 'Pipeline completed. Checking for any resources left running.'
                sh 'docker ps'
            }
        }
    }
}
