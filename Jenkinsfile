pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cleaning workspace...'
                cleanWs() // Make sure to install "Workspace Cleanup Plugin"
                
                echo 'Checking out code...'
                git branch: 'main', url: 'https://github.com/amreen235/todolist1.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask app...'
                dir('backend') { // since requirements.txt is inside backend
                    sh 'python3 -m venv venv' // Create virtual environment
                    sh '. venv/bin/activate && pip install -r requirements.txt' // Activate venv and install dependencies
                }
            }
        }

        stage('Run Test') {
            steps {
                echo 'Running tests...'
                // Add test commands here if needed, e.g. pytest
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask app...'
                // Add deployment logic if needed
            }
        }
    }
}
