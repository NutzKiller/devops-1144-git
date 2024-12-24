pipeline {
    agent any
    environment {
        DB_HOST = credentials('db_host')
        DB_USER = credentials('db_user')
        DB_PASSWORD = credentials('db_password')
        DB_NAME = credentials('db_name')
        PORT = '5000'  // Non-sensitive, so we define it directly
        IMAGE_NAME = 'nutzkiller/flask_catgif_clean'  // Docker Hub image name
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
                    // Fetch the latest Git tag
                    def latestTag = sh(script: "git describe --tags --abbrev=0", returnStdout: true).trim()
                    echo "Latest Git tag: $latestTag"

                    // Increment the version (patch version)
                    def versionParts = latestTag.tokenize('.')
                    def major = versionParts[0]
                    def minor = versionParts[1]
                    def patch = versionParts[2].toInteger() + 1 // Increment patch version by 1
                    VERSION = "${major}.${minor}.${patch}"
                    echo "Generated new version: $VERSION"

                    // Tag the commit with the new version
                    sh "git tag -a $VERSION -m 'Release version $VERSION'"
                    sh "git push origin $VERSION"
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
                echo "Resources left running"
                // Optionally stop the Docker containers after pushing to Docker Hub
                // docker-compose down could be added here if needed
            }
        }
    }
}
