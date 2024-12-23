pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')  // Poll SCM every minute
    }

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
                    withCredentials([string(credentialsId: 'flask_env', variable: 'FLASK_ENV')]) {
                        // Split the FLASK_ENV string and set each environment variable
                        def envVars = FLASK_ENV.split('\n')
                        envVars.each { line ->
                            def (key, value) = line.split('=')
                            env[key] = value  // Set the environment variables for Docker Compose
                        }

                        // Print out the environment variables (optional, for debugging)
                        echo "PORT: ${env.PORT}"
                        echo "DB_HOST: ${env.DB_HOST}"
                        echo "DB_USER: ${env.DB_USER}"
                        echo "DB_PASSWORD: ${env.DB_PASSWORD}"
                        echo "DB_NAME: ${env.DB_NAME}"

                        // Create .env file for Docker Compose with secrets
                        sh """
                        cd devops-1144-git/flask_catgif_clean
                        echo "PORT=${env.PORT}" >> .env
                        echo "DB_HOST=${env.DB_HOST}" >> .env
                        echo "DB_USER=${env.DB_USER}" >> .env
                        echo "DB_PASSWORD=${env.DB_PASSWORD}" >> .env
                        echo "DB_NAME=${env.DB_NAME}" >> .env
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

                    // Test if the app is running
                    sh '''
                    if ! curl -f http://localhost:${env.PORT}; then
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
