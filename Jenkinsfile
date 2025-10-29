pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t mycontainerapp"
            }
        } 
        stage('run') {
            steps {
                echo "Run the container"
                bat "docker rm -f mycontainerapp || exit 0"
                bat "docker run -d -p mycontainerapp sreeshvini4/demoapp:t1"
            }
        }
    }
    post {
        Success {
            echo "Connection successful"
        }
        Failure {
            echo "Failure in connecting, check logs"
        }
    }
}