pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/your-username/your-repo.git'  // Replace with your actual repository URL
        IMAGE_NAME = 'my-jenkins-docker'  // Replace with your Docker image name
        CONTAINER_NAME = 'my-jenkins-docker'  // Replace with your container name
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository manually...'
                sh "git clone ${REPO_URL} repo"
            }
        }

        stage('Checkout Code') {
            steps {
                echo 'Checking out source code...'
                dir('repo') {
                    sh 'ls -la'  // This will list the files in the repo folder to ensure it's cloned
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                dir('repo') {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                echo 'Stopping old container (if running)...'
                sh "docker stop ${CONTAINER_NAME} || true"
            }
        }

        stage('Remove Old Container') {
            steps {
                echo 'Removing old container (if exists)...'
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }

        stage('Run New Container') {
            steps {
                echo 'Running new container...'
                sh "docker run -d --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }

        stage('List Running Containers') {
            steps {
                echo 'Listing running Docker containers...'
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
