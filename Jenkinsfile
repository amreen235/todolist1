pipeline {
    agent any

    environment {
        PROJECT_NAME         = 'todolist1'  // Aligning with your project name
        IMAGE_NAME           = "${PROJECT_NAME}:latest"
        DOCKER_REGISTRY      = 'docker.io/myorg'  // Replace with your Docker registry if needed
        REGISTRY_CREDENTIALS = 'dockerhub-creds'  // Credentials for Docker registry
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out source code...'
                script {
                    // If SCM is defined in Jenkins, use it, otherwise fetch from GitHub
                    if (scm) {
                        checkout scm
                    } else {
                        checkout([
                            $class: 'GitSCM',
                            branches: [[name: '*/main']],  // Change this to your branch if different
                            userRemoteConfigs: [[url: 'https://github.com/amreen235/todolist1.git']]  // Your repo URL
                        ])
                    }
                }
            }
        }

        stage('Build Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}"
                script {
                    // Docker build command, without sudo as Jenkins user has Docker permissions
                    sh '''
                        #!/bin/bash
                        export DOCKER_BUILDKIT=1
                        docker build -t ${IMAGE_NAME} .
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                    script {
                        // Running tests inside the Docker container
                        sh '''
                            #!/bin/bash
                            docker run --rm ${IMAGE_NAME} npm test
                        '''
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying app...'
                script {
                    // Stop and remove any existing container before running the new one
                    sh '''
                        #!/bin/bash
                        docker stop ${PROJECT_NAME} || true
                        docker rm ${PROJECT_NAME} || true
                        docker run -d --name ${PROJECT_NAME} -p 3000:3000 ${IMAGE_NAME}
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up unused resources...'
            script {
                // Prune Docker system to remove unused containers, images, networks, etc.
                sh '''
                    #!/bin/bash
                    docker system prune -f || true
                '''
            }
        }
    }
}
