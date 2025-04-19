pipeline {
    agent any

    stages {
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
                // Add test commands here if needed
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask app...'
                // Add deploy steps
            }
        }
    }
}
