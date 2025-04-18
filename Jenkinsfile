pipeline {
    agent any

    environment {
        PROJECT_NAME         = 'todolist1'
        IMAGE_NAME           = "${PROJECT_NAME}:latest"
        DOCKER_REGISTRY      = 'docker.io/myorg'
        REGISTRY_CREDENTIALS = 'dockerhub-creds'
    }

    stages {
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

        stage('Build Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}"
                sh 'export DOCKER_BUILDKIT=1'
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                    sh "docker run --rm ${IMAGE_NAME} npm test"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying app...'
                sh "docker stop ${PROJECT_NAME} || true"
                sh "docker rm ${PROJECT_NAME} || true"
                sh "docker run -d --name ${PROJECT_NAME} -p 3000:3000 ${IMAGE_NAME}"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up unused resources...'
            sh "docker system prune -f || true"
        }
    }
}
