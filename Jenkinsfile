pipeline {
    agent any

    options {
        timeout(time: 15, unit: 'MINUTES')
    }

    tools {
        allure 'allure'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/amritasak27/Automation-Project.git'
            }
        }

        stage('BDD Framework - Setup & Test') {
            steps {
                dir('bdd-framework') {
                    bat '''
                        py -3.11 -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        playwright install chromium
                        pytest --junitxml=reports\\report.xml
                    '''
                }
            }
        }
    }

    post {
        always {
            junit 'bdd-framework/reports/report.xml'
            allure includeProperties: false, jdk: '', results: [
                [path: 'bdd-framework/reports/allure-results']
            ]
        }
        failure {
            echo 'Tests failed.'
        }
    }
}