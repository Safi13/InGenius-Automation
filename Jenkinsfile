pipeline {
    agent any

    stages {
        stage('Install Project Dependencies') {
            steps {
                // Install project dependencies
                sh 'pip3.11 install -r requirements.txt'
            }
        }

        stage('Run Tests with Allure Formatting') {
            steps {
                // Run your tests with the AllureFormatter
                sh '~/.local/bin/behave --format allure_behave.formatter:AllureFormatter -o allure-results'
            }
        }

//         stage('Generate and View Allure Report') {
//             steps {
//                 // Generate and serve Allure report
//                 sh 'allure serve'
//             }
//         }
    }
}
