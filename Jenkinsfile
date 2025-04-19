pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
               git branch: 'main', git url: 'https://github.com/amreen235/todolist1.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask app...'
                // Add your build commands here, like 'sh "pip install -r requirements.txt"'
            }
        }

        stage('Run Test') {
            steps {
                echo 'Running tests...'
                // Add your test commands here, like 'sh "pytest"'
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
