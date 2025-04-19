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
        
        // Create and activate virtual environment (Windows)
        bat 'python -m venv venv'  // Create virtual environment for Windows
        bat 'venv\\Scripts\\activate'  // Activate virtual environment for Windows
        bat 'pip install -r requirements.txt'  // Install dependencies
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
