pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/ShreeyaVenneti/IMT2020535_SE_Assignment6.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x fibonacci_function.py"
                sh "./fibonacci_function.py"
            }
        }
        stage('Passing Test Code') {
            steps {
                sh "chmod u+x Passing_UnitTests.py"
                sh "./Passing_UnitTests.py"
            }
        }
        stage('Failing Test Code') {
            steps {
                sh "chmod u+x Failing_UnitTests.py"
                sh "./Failing_UnitTests.py"
            }
        }
    } 
}
