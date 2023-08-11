pipeline {
    agent any

    stages {
        stage('Install Allure Dependencies') {
            steps {
                bat 'choco install allure-commandline' // Install Allure using Chocolatey package manager
            }
        }

        stage('Python Setup') {
            steps {
                bat 'python -m venv venv' // Use 'bat' for Windows shell commands
                bat 'venv\\Scripts\\activate' // Activate the virtual environment
                bat 'pip install -r requirements.txt' // Install Python dependencies
            }
        }

        stage('Run Tests') {
            steps {
                bat 'behave --format allure_behave.formatter:AllureFormatter -o allure-results' // Run tests and generate Allure report
            }
        }

        stage('Generate and View Allure Report') {
            steps {
                bat 'allure serve allure-results' // Generate and serve the Allure report
            }
        }
    }

    post {
        always {
            bat 'venv\\Scripts\\deactivate' // Deactivate the virtual environment
        }
    }
}
