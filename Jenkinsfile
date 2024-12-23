pipeline {
    agent any

<<<<<<< HEAD
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
=======
    triggers {
        pollSCM('* * * * *')  // Poll SCM every minute
    }
>>>>>>> aafbb85501b61a3c578dae784479378c12be2edb

    environment {
        // Inject secrets into environment variables
        PORT = credentials('PORT_SECRET')
        DB_HOST = credentials('DB_HOST_SECRET')
        DB_USER = credentials('DB_USER_SECRET')
        DB_PASSWORD = credentials('DB_PASSWORD_SECRET')
        DB_NAME = credentials('DB_NAME_SECRET')
    }

    stages {
        stage('Cleanup') {
            steps {
                script {
<<<<<<< HEAD
<<<<<<< HEAD
                    // Stop and remove any existing containers
=======
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
=======
                    // Stop and remove any existing containers
>>>>>>> aafbb85501b61a3c578dae784479378c12be2edb
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down || echo "No containers to stop or remove"'
                }
            }
        }
        stage('Build') {
            steps {
                script {
<<<<<<< HEAD
<<<<<<< HEAD
                    // Clone the repository and build Docker images
=======
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
=======
                    // Clone the repository and build Docker images
>>>>>>> aafbb85501b61a3c578dae784479378c12be2edb
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
<<<<<<< HEAD
=======
>>>>>>> aafbb85501b61a3c578dae784479378c12be2edb
                    // Start the containers using Docker Compose
                    sh '''
                    cd devops-1144-git/flask_catgif_clean
                    PORT=${PORT} DB_HOST=${DB_HOST} DB_USER=${DB_USER} DB_PASSWORD=${DB_PASSWORD} DB_NAME=${DB_NAME} docker-compose up -d
                    '''
<<<<<<< HEAD
=======
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose up -d'
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
=======
>>>>>>> aafbb85501b61a3c578dae784479378c12be2edb
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Wait for the container to start
                    sh 'sleep 5'
<<<<<<< HEAD
<<<<<<< HEAD
                    
                    // Test if the app is running
=======
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
=======
                    
                    // Test if the app is running
>>>>>>> aafbb85501b61a3c578dae784479378c12be2edb
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
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Cleanup After Run') {
            steps {
                script {
<<<<<<< HEAD
<<<<<<< HEAD
                    // Stop and clean up containers
=======
>>>>>>> 0491df56209eef1acb911b1682f08a631cf0bd6b
=======
                    // Stop and clean up containers
>>>>>>> aafbb85501b61a3c578dae784479378c12be2edb
                    sh 'cd devops-1144-git/flask_catgif_clean && docker-compose down'
                }
            }
        }
    }
}
