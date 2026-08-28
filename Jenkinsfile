pipeline {
    agent any

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
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pytest --junitxml=report.xml --alluredir=allure-results
                    '''
                }
            }
        }

        stage('Data-Driven Framework - Setup & Test') {
            steps {
                dir('data-driven-framework') {
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pytest --junitxml=report.xml --alluredir=allure-results
                    '''
                }
            }
        }
    }

    post {
        always {
            junit 'bdd-framework/report.xml, data-driven-framework/report.xml'
            allure includeProperties: false, jdk: '', results: [
                [path: 'bdd-framework/allure-results'],
                [path: 'data-driven-framework/allure-results']
            ]
        }
        failure {
            echo 'Tests failed.'
        }
    }
}