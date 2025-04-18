pipeline {
    agent any

    environment {
        IMAGE_NAME = 'todolist-app'
        CONTAINER_NAME = 'todolist-container'
        APP_PORT = '8080' // Updated port to 8080
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/amreen235/todolist1.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🔧 Building Docker Image...'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo '🚀 Running Docker Container...'
                // Stop & remove existing container if running
                sh '''
                    docker rm -f $CONTAINER_NAME || true
                    docker run -d -p $APP_PORT:$APP_PORT --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
    }
}
