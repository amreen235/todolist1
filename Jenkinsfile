pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                git url: 'https://github.com/amreen235/todolist1.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask app...'
                // We'll add specific build steps later
            }
        }

        stage('Run Test') {
            steps {
                echo 'Running tests...'
                // Test commands go here
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask app...'
                // Deployment steps will go here
            }
        }
    }
}
