pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t mydockerimg"
            }
        } 
        stage('run') {
            steps {
                echo "Run the container"
                bat "docker rm -f mydockerimg || exit 0"
                bat "docker run -d -p mydockerimg sreeshvini4/mycontainerapp:t1"
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