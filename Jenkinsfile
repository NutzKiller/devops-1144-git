pipeline {
    agent any
    environment {
        // Inject the Jenkins secret 'flask_env'
        FLASK_ENV = credentials('flask_env') 
    }
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage('Cleanup Old Repo') {
            steps {
                echo "Removing old repo if it exists"
                sh 'rm -rf devops-1144-git'
            }
        }
        stage('Checkout Repo') {
            steps {
                echo "Cloning repository"
                sh 'git clone https://github.com/nutzkiller/devops-1144-git.git'
            }
        }
        stage('Docker Compose Up') {
            steps {
                dir('devops-1144-git/flask_catgif_clean') {
                    echo "Starting Docker Compose"
                    sh '''
                        # Export environment variables from Jenkins secret
                        export $(echo $FLASK_ENV | tr ',' '\\n' | xargs)
                        
                        docker-compose down
                        docker-compose up -d
                    '''
                }
            }
        }
        stage('Health Check') {
            steps {
                script {
                    def response = sh(script: "curl -f http://localhost:5000", returnStatus: true)
                    if (response != 0) {
                        error "Health check failed! Flask app is not reachable."
                    } else {
                        echo "Health check passed! Flask app is running."
                    }
                }
            }
        }
    }
    post {
        always {
            echo "Cleanup resources"
            dir('devops-1144-git/flask_catgif_clean') {
                sh 'docker-compose down'
            }
        }
    }
}
