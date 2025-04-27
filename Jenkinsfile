pipeline {
    agent any

    parameters {
        string(name: 'user_id', defaultValue: '', description: 'Enter your user ID')
        password(name: 'user_password', defaultValue: '', description: 'Enter your user password') // still defined as password input
    }

    stages {
        stage('UserCheckIn') {
            steps {
                echo "User ID entered: ${params.user_id}"
                echo "User Password entered (visible for practice): ${params.user_password}" // 👈 shows it in logs
            }
            post {
                success {
                    echo 'User check-in completed successfully.'
                }
                failure {
                    echo 'User check-in failed.'
                }
            }
        }

        stage('CheckOut') {
            steps {
                echo 'Git Action based performing'
            }
            post {
                success {
                    echo 'CheckOut stage completed successfully.'
                }
                failure {
                    echo 'CheckOut stage failed.'
                }
            }
        }

        stage('testing') {
            steps {
                echo 'Testing is going on'
            }
            post {
                success {
                    echo 'Testing stage completed successfully.'
                }
                failure {
                    echo 'Testing stage failed.'
                }
            }
        }

        stage('deploying') {
            steps {
                echo 'Deploying is done'
            }
            post {
                success {
                    echo 'Deploying stage completed successfully.'
                }
                failure {
                    echo 'Deploying stage failed.'
                }
            }
        }
    }
}
