pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u root'  // Run container as root so we can install if needed
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/amreen235/todolist1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing Python dependencies...'
                sh '''
                    apt-get update && apt-get install -y bash coreutils
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r backend/requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '✅ Tests can be added here later.'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploy stage placeholder.'
            }
        }
    }
}
