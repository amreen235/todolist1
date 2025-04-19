pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                echo 'Cleaning workspace...'
                cleanWs()
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask app...'
                dir('backend') {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Test') {
            steps {
                echo 'Running tests...'
                // e.g. sh 'pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask app...'
                // Add deployment logic here
            }
        }
    }
}
