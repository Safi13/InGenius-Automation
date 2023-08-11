pipeline {
  agent any

    stages {
        stage('Install Allure Dependencies') {
            steps {
                sh 'sudo apt-add-repository ppa:qameta/allure'
                sh 'sudo apt-get update'
                sh 'sudo apt-get install allure'
            }
        }

        stage('Python Setup') {
            steps {
                // Create and activate Python virtual environment
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'

                // Install project dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests with the AllureFormatter
                sh 'behave --format allure_behave.formatter:AllureFormatter -o allure-results'
            }
        }

        stage('Generate and View Allure Report') {
            steps {
                // Generate Allure report
                sh 'allure serve'
            }
        }
    }

    post {
        always {
            sh 'deactivate'
        }
    }
}
