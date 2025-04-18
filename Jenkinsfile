pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[
                        url: 'https://github.com/amreen235/todolist1.git'
                    ]]
                ])
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker Compose services...'
                sh 'docker-compose -p todolist1 build'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Skipping tests for now...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application using Docker Compose...'
                sh 'docker-compose -p todolist1 up -d'
            }
        }
    }
}