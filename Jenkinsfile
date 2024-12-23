pipeline {
    agent any

    stages {
        stage('Prepare .env') {
            steps {
                script {
                    // Copy the .env file from the desktop to the project folder
                    sh 'cp /home/yuval3/Desktop/.env devops-1144-git/flask_catgif_clean/.env'
                    // Verify the file was copied correctly
                    sh 'cat devops-1144-git/flask_catgif_clean/.env'
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down || echo "No containers to stop or remove"'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'rm -rf devops-1144-git'
                    sh 'git clone https://github.com/NutzKiller/devops-1144-git.git'
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'sleep 5'
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
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down'
                }
            }
        }
    }
}
