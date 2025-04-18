pipeline { agent any

options {
    // Retry flaky failures
    retry(3)
    // Abort if the pipeline runs longer than 30 minutes
    timeout(time: 30, unit: 'MINUTES')
}

environment {
    PROJECT_NAME         = 'todolist1'
    IMAGE_NAME           = "${PROJECT_NAME}:latest"
    DOCKER_REGISTRY      = 'docker.io/myorg'
    REGISTRY_CREDENTIALS = 'dockerhub-creds'
}

stages {
    stage('Checkout') {
        steps {
            echo 'Checking out code...'
            script {
                if (scm) checkout scm
                else checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/amreen235/todolist1.git']]
                ])
            }
        }
    }

    stage('Verify Docker') {
        steps {
            echo 'Verifying Docker installation...'
            // Return status so failure won't abort
            sh(script: 'docker --version', returnStatus: true)
        }
    }

    stage('Build Image') {
        steps {
            echo "Building Docker image ${IMAGE_NAME}..."
            script {
                // Build with BuildKit enabled on the agent
                sh 'export DOCKER_BUILDKIT=1'
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }
    }

    stage('Run Tests') {
        steps {
            echo 'Running tests inside Docker container...'
            catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                sh "docker run --rm ${IMAGE_NAME} npm test"
            }
        }
    }

    stage('Push Image') {
        steps {
            echo "Pushing image to ${DOCKER_REGISTRY}..."
            script {
                docker.withRegistry("https://${DOCKER_REGISTRY}", REGISTRY_CREDENTIALS) {
                    sh "docker tag ${IMAGE_NAME} ${DOCKER_REGISTRY}/${IMAGE_NAME}"
                    sh "docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}"
                }
            }
        }
    }

    stage('Deploy') {
        steps {
            echo 'Deploying container...'
            script {
                // Stop and remove any existing container
                sh "docker stop ${PROJECT_NAME} || true"
                sh "docker rm ${PROJECT_NAME} || true"
                // Run new container, adjust ports as needed
                sh "docker run -d --name ${PROJECT_NAME} -p 3000:3000 ${DOCKER_REGISTRY}/${IMAGE_NAME}"
            }
        }
    }
}

post {
    always {
        echo 'Cleaning up dangling images and containers...'
        sh "docker system prune -f || true"
    }
}

}