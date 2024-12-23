pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')  // Poll SCM every minute
    }

    stages {
        stage('Cleanup') {
            steps {
                sh '''
                docker stop flask_app_container || echo "Container not running"
                docker rm flask_app_container || echo "Container already removed"
                '''
            }
        }
        stage('Build') {
            steps {
                sh 'rm -rf devops-1144-git'
                sh 'git clone https://github.com/NutzKiller/devops-1144-git.git'
                sh 'cd devops-1144-git/flask_catgif_clean && docker build -t flask_app .'
            }
        }
        stage('Run') {
            steps {
                sh '''
                docker ps -a  # List containers to check if there's a conflict
                docker run --rm -d -p 5000:5000 --name flask_app_container flask_app
                docker ps  # Verify if the container is running
                '''
            }
        }
        stage('Test') {
            steps {
                // Wait for the container to start
                sh 'sleep 5'
                // Check logs for errors
                sh '''
                if ! docker logs flask_app_container; then
                    echo "Container logs check failed"
                    exit 1
                fi
                '''
                // Test the app
                sh '''
                if ! curl -f http://localhost:5000; then
                    echo "App is not reachable."
                    docker logs flask_app_container
                    exit 1
                fi
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
