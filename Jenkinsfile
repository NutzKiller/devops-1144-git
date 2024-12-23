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
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose build'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Navigate to the flask_catgif_clean directory and start the container using docker-compose
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose up -d'
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
