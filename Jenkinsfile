pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/amreen235/todolist1.git'
            }
        }

        stage('Build') {
            steps {
                echo '📦 Installing Python dependencies...'
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
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
