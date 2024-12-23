pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the latest changes from the repo
                    checkout scm
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Clone the repository and build Docker images
                    sh 'rm -rf devops-1144-git'
                    sh 'git clone https://github.com/NutzKiller/devops-1144-git.git'

                    // Use withCredentials to inject 'flask_env' secret as environment variables
                    withCredentials([string(credentialsId: 'flask_env', variable: 'flask_env')]) {
                        echo "flask_env: ${flask_env}"

                        // Split the flask_env string into individual key-value pairs
                        def envVars = flask_env.split('\n')
                        def envMap = [:]
                        envVars.each { line ->
                            def (key, value) = line.split('=')
                            if (key && value) {
                                envMap[key.trim()] = value.trim()  // Store in the map
                                echo "Setting environment variable: ${key.trim()} = ${value.trim()}"
                            }
                        }

                        // Print out the environment variables (optional, for debugging)
                        echo "PORT: ${envMap['PORT']}"
                        echo "DB_HOST: ${envMap['DB_HOST']}"
                        echo "DB_USER: ${envMap['DB_USER']}"
                        echo "DB_PASSWORD: ${envMap['DB_PASSWORD']}"
                        echo "DB_NAME: ${envMap['DB_NAME']}"

                        // Create .env file for Docker Compose with secrets
                        sh """
                        cd devops-1144-git/flask_catgif_clean
                        echo "PORT=${envMap['PORT']}" > .env
                        echo "DB_HOST=${envMap['DB_HOST']}" >> .env
                        echo "DB_USER=${envMap['DB_USER']}" >> .env
                        echo "DB_PASSWORD=${envMap['DB_PASSWORD']}" >> .env
                        echo "DB_NAME=${envMap['DB_NAME']}" >> .env
                        docker-compose build
                        """
                    }
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

                    // Test if the app is running using bash for variable substitution
                    sh '''
                    if ! curl -f http://localhost:$PORT; then
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

        stage('Cleanup') {
            steps {
                script {
                    // Stop and clean up containers
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down'
                }
            }
        }
    }
}
