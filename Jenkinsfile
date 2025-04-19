pipeline {
    agent any

    environment {
        PROJECT_NAME     = 'todolist1'
        IMAGE_NAME       = "${PROJECT_NAME}:latest"
        CONTAINER_NAME   = 'todolist1-container'
        PORT             = '3000'
        DOCKER_REGISTRY  = 'docker.io/myorg'
        REGISTRY_CREDENTIALS = 'dockerhub-creds'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Repository is automatically cloned by Jenkins (SCM configured)'
            }
        }

        stage('Checkout Code') {
            steps {
                echo 'Checking out source code...'
                script {
                    if (scm) {
                        checkout scm
                    } else {
                        checkout([
                            $class: 'GitSCM',
                            branches: [[name: '*/main']],
                            userRemoteConfigs: [[url: 'https://github.com/amreen235/todolist1.git']]
                        ])
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}"
                sh '''
                    docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                echo 'Stopping any existing container...'
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Remove Old Container') {
            steps {
                echo 'Removing any existing container...'
                sh '''
                    docker rm ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                echo 'Running new container...'
                sh '''
                    docker run -d -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}
                '''
            }
        }

        stage('List Running Containers') {
            steps {
                echo 'Listing all running containers...'
                sh 'docker ps'
            }
        }
    }

    post {
        always {
            echo 'Pipeline run finished.'
        }
    }
}
