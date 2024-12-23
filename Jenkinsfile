pipeline {
    agent any

<<<<<<< HEAD
    triggers {
        pollSCM('* * * * *')  // Poll SCM every minute
    }

    environment {
        // Inject secrets into environment variables
        PORT = credentials('PORT_SECRET')
        DB_HOST = credentials('DB_HOST_SECRET')
        DB_USER = credentials('DB_USER_SECRET')
        DB_PASSWORD = credentials('DB_PASSWORD_SECRET')
        DB_NAME = credentials('DB_NAME_SECRET')
    }

=======
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
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
<<<<<<< HEAD
                    // Stop and remove any existing containers
=======
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down || echo "No containers to stop or remove"'
                }
            }
        }

        stage('Build') {
            steps {
                script {
<<<<<<< HEAD
                    // Clone the repository and build Docker images
=======
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
                    sh 'rm -rf devops-1144-git'
                    sh 'git clone https://github.com/NutzKiller/devops-1144-git.git'
                    sh '''
                    cd devops-1144-git/flask_catgif_clean
                    PORT=${PORT} DB_HOST=${DB_HOST} DB_USER=${DB_USER} DB_PASSWORD=${DB_PASSWORD} DB_NAME=${DB_NAME} docker-compose build
                    '''
                }
            }
        }

        stage('Run') {
            steps {
                script {
<<<<<<< HEAD
                    // Start the containers using Docker Compose
                    sh '''
                    cd devops-1144-git/flask_catgif_clean
                    PORT=${PORT} DB_HOST=${DB_HOST} DB_USER=${DB_USER} DB_PASSWORD=${DB_PASSWORD} DB_NAME=${DB_NAME} docker-compose up -d
                    '''
=======
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose up -d'
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'sleep 5'
<<<<<<< HEAD
                    
                    // Test if the app is running
=======
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
                    sh '''
                    if ! curl -f http://localhost:${PORT}; then
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
<<<<<<< HEAD
                    // Stop and clean up containers
=======
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down'
                }
            }
        }
    }
}
