pipeline {
    agent any

    stages {
        stage('CHECKOUT') {
            steps {
                echo 'Cleaning workspace...'
                cleanWs() // Clean workspace before checkout
                echo 'Checking out the code from the repository...'
                git branch: 'main', url: 'https://github.com/amreen235/todolist1.git'
            }
        }

        stage('BUILD') {
            steps {
                echo 'Building Flask app...'
                dir('backend') { // Assuming your Flask app is inside the 'backend' folder
                    echo 'Checking Python version...'
                    sh 'python3 --version' // Verify Python is installed
                    echo 'Creating virtual environment...'
                    sh 'python3 -m venv venv' // Create virtual environment
                    echo 'Activating virtual environment and installing dependencies...'
                    sh '''#!/bin/bash
                        source venv/bin/activate
                        pip install -r requirements.txt
                    ''' // Activate venv and install dependencies
                }
            }
        }

        stage('UNIT TEST CASE') {
            steps {
                echo 'Running unit tests...'
                // Add test commands here (e.g., pytest, unittest)
            }
        }

        stage('DEPLOY') {
            steps {
                echo 'Deploying Flask app...'
                // Add deployment logic if needed (e.g., push to a server, Docker, etc.)
            }
        }
    }
}
