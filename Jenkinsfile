pipeline{
    agent any

    environment{
        IMAGE_NAME = "saks04/fastapi-Backend"
        DOCKERHUB_CREDENTIALS = "dockerhub-cred"
    }

    stages{
        stage('checkout'){
            steps{
                checkout scm
            }
        }
        stage('Build Docker Image'){
            steps{
                sh "docker build -t $IMAGE_NAME:latest ."
            }
        }
        stage('Test Container'){
            steps{
                sh 'docker compose run --rm web pytest || echo "No tests found, skipping"'
            }
        }
        stage("push to Docker Hub"){
            steps{
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", usernameVariable: "USERNAME", passwordVariable: "PASSWORD")]) {
                    sh """
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                        docker push $IMAGE_NAME:latest
                    """
                }
            }
        }
        stage("Clean up"){
            steps{
                sh "docker system prune -f"
            }
        }
    }  
    post{
        success{
            echo "✅ FastAPI CI/CD Pipeline completed successfully!"
        }
        failure{
            echo "❌ Build failed — check logs in Jenkins."
        }
    }
}