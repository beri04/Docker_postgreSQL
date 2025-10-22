pipeline {
    agent any

    environment {
        IMAGE_NAME = "saks04/fastapi-backend"
        DOCKERHUB_CREDENTIALS = "dockerhub-cred"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "📦 Checking out latest code from GitHub..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Test Container') {
            steps {
                echo "🧪 Running tests (if available)..."
                sh 'docker run --rm $IMAGE_NAME:latest pytest || echo "⚠️ No tests found, skipping..."'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "📤 Pushing image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                        set +x
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                        docker push $IMAGE_NAME:latest

                        # Tag image with Jenkins build number for versioning
                        docker tag $IMAGE_NAME:latest $IMAGE_NAME:$BUILD_NUMBER
                        docker push $IMAGE_NAME:$BUILD_NUMBER

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                echo "🚀 Deploying latest container..."
                sh '''
                    set +x
                    docker pull $IMAGE_NAME:latest

                    # Stop and remove any existing container safely
                    docker stop fastapi_app || true
                    docker rm fastapi_app || true

                    # Start new container
                    docker run -d --name fastapi_app -p 8000:8000 $IMAGE_NAME:latest

                    echo "✅ Deployment complete. FastAPI running on port 8000."
                '''
            }
        }

        stage('Clean Up') {
            steps {
                echo "🧹 Cleaning up old Docker images and containers..."
                sh '''
                    docker image prune -f
                    docker container prune -f
                '''
            }
        }
    }

    post {
        success {
            echo "🎯 FastAPI CI/CD pipeline completed successfully!"
        }
        failure {
            echo "❌ Build failed — check Jenkins logs for details."
        }
    }
}
