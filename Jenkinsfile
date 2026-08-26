pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main' ,url:https://github.com/amritasak27/Automation-Project'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=report.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
        failure {
            echo 'Tests failed.'
        }
    }
}