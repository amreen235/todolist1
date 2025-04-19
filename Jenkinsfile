pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                git branch: 'main', url: 'https://github.com/amreen235/todolist1.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask app...'
                // Create and activate virtual environment
                sh 'python3 -m venv venv'  // Create virtual environment
                sh 'source venv/bin/activate'  // Activate virtual environment (for Linux/macOS, use venv\\Scripts\\activate for Windows)
                sh 'pip install -r requirements.txt'  // Install dependencies
            }
        }

        stage('Run Test') {
            steps {
                echo 'Running tests...'
                // You can add test commands here, like 'sh "pytest"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask app...'
                // Add deployment commands here, like 'sh "./deploy.sh"'
            }
        }
    }
}
