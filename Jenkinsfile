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
                sh '''
                    set +x
                    docker build -t $IMAGE_NAME:latest .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "📤 Pushing Docker image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                        set +x
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                        docker push $IMAGE_NAME:latest

                        # Optional: Tag image with Jenkins build number
                        docker tag $IMAGE_NAME:latest $IMAGE_NAME:$BUILD_NUMBER
                        docker push $IMAGE_NAME:$BUILD_NUMBER

                        docker logout
                    '''
                }
            }
        }

        stage('Check Compose') {
            steps {
                echo "⚙️ Checking Docker Compose availability..."
                sh 'docker-compose --version'
            }
        }

        stage('Deploy Container') {
            steps {
                echo "🚀 Deploying FastAPI + PostgreSQL via Docker Compose..."
                sh '''
                    set +x

                    echo "⚙️ Checking Docker Compose availability..."
                    if docker compose version > /dev/null 2>&1; then
                        echo "✅ Docker Compose is already available."
                    else
                        echo "⚠️ Docker Compose not found. Installing..."
                        apt-get update && apt-get install -y docker-compose || true
                    fi

                    echo "🧱 Starting deployment stack..."
                    docker compose down || true
                    docker compose up -d --build

                    echo "✅ FastAPI + PostgreSQL deployed successfully on port 8000."
                '''
            }   
        }


        stage('Verify Deployment') {
            steps {
                echo "🔍 Checking running containers..."
                sh '''
                    docker ps
                    echo "🌐 Visit your FastAPI app at: http://<EC2_PUBLIC_IP>:8000/docs"
                '''
            }
        }
    }

    post {
        success {
            echo "🎯 CI/CD Pipeline executed successfully!"
        }
        failure {
            echo "❌ Pipeline failed — check the Jenkins logs for details."
        }
        always {
            echo "🧹 Cleaning temporary build resources..."
        }
    }
}
