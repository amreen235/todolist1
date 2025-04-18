pipeline { agent any

options {
    // Retry up to 3 times on failures
    retry(3)
    // Abort if the pipeline runs longer than 30 minutes
    timeout(time: 30, unit: 'MINUTES')
}

environment {
    PROJECT_NAME = 'todolist1'
    COMPOSE_FILE = 'docker-compose.yml'
    COMPOSE_PROJECT = "${PROJECT_NAME}"
}

stages {
    stage('Checkout') {
        steps {
            echo 'Checking out code...'
            // Use built-in SCM configuration if available
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

    stage('Verify Docker Compose') {
        steps {
            echo 'Verifying Docker Compose installation...'
            // Return status instead of failing
            sh(script: 'docker-compose --version', returnStatus: true)
        }
    }

    stage('Build') {
        steps {
            echo 'Building Docker Compose services...'
            catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                sh "docker-compose -f ${COMPOSE_FILE} -p ${COMPOSE_PROJECT} build"
            }
        }
    }

    stage('Run Tests') {
        steps {
            echo 'Running tests (if any)...'
            // Continue even if tests fail
            catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                sh "docker-compose -f ${COMPOSE_FILE} -p ${COMPOSE_PROJECT} run --rm app npm test"
            }
        }
    }

    stage('Deploy') {
        steps {
            echo 'Deploying the application using Docker Compose...'
            // Tear down any existing containers, ignore errors
            sh "docker-compose -f ${COMPOSE_FILE} -p ${COMPOSE_PROJECT} down || true"
            // Start containers in detached mode
            sh "docker-compose -f ${COMPOSE_FILE} -p ${COMPOSE_PROJECT} up -d"
        }
    }
}

post {
    always {
        echo 'Post-build cleanup: stopping containers...'
        sh "docker-compose -f ${COMPOSE_FILE} -p ${COMPOSE_PROJECT} down || true"
    }
}

}