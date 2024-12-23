pipeline {
    agent any

    stages {
        stage('Prepare .env') {
            steps {
                script {
                    // Copy the .env file from the desktop to the project folder
                    sh 'cp /home/yuval3/Desktop/.env devops-1144-git/flask_catgif_clean/.env'
                }
            }
        }

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
                    sh 'rm -rf devops-1144-git'
                    sh 'git clone https://github.com/NutzKiller/devops-1144-git.git'
                    sh 'cat devops-1144-git/flask_catgif_clean/.env'
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
