# FastAPI CI/CD Pipeline on AWS EC2

Automated CI/CD pipeline built with Jenkins, Docker, and AWS EC2, deploying a FastAPI + PostgreSQL backend.
Every push to GitHub triggers Jenkins → builds Docker image → scans → pushes to Docker Hub → deploys containerized app automatically.

# 🧩 Architecture Overview
![alt text](<image.png>)

(Diagram: AWS EC2 → Docker Engine → Jenkins → Docker Hub / FastAPI + Swagger UI / PostgreSQL)

# 🛠️ Tech Stack
Layer	                  Tools Used
Cloud & Infra	          AWS EC2, Docker Engine
CI/CD	                  Jenkins (Declarative Pipeline)
Backend	                  FastAPI, Swagger UI
Database                  PostgreSQL
Container Registry	      Docker Hub
Code Repo	              GitHub (Webhook Trigger)


# ⚙️ Pipeline Flow
1️⃣ Code Commit → Developer pushes to GitHub
2️⃣ Webhook Trigger → Jenkins pipeline starts automatically
3️⃣ Build Stage → Jenkins builds Docker image of FastAPI app
4️⃣ Image Scan → Checks for vulnerabilities
5️⃣ Push Stage → Pushes image to Docker Hub
6️⃣ Deploy Stage →
 • Runs container for FastAPI + Swagger UI
 • Runs PostgreSQL container
 • Connects both in a private Docker network
7️⃣ Verify Stage → App accessible via EC2 Public IP :8000/docs

# 🧾 Project Structure
fastapi-backend/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   └── database.py
│
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
└── README.md

# 🚀 Deployment Steps (Short)
**1. Clone repo**
git clone https://github.com/saks04/fastapi-backend.git
cd fastapi-backend

**2. Build and run locally (optional)**
docker-compose up --build

**3. CI/CD handled by Jenkins on EC2**
    → Pulls latest code
    → Builds Docker image
    → Pushes to Docker Hub
    → Deploys FastAPI + PostgreSQL containers

# 🧠 Key Learnings

End-to-end DevOps automation using Jenkins Declarative Pipeline

Multi-container orchestration via Docker Compose

Secure database connection inside private Docker network

AWS EC2 as a persistent host for Jenkins and FastAPI services

Real-world debugging of build failures, Docker credential issues, and webhooks

# 🏷️ Badges








# 🧑‍💻 Author

Saksham Beri
Backend & DevOps Engineer | FastAPI • Docker • Jenkins • AWS

# 🔗 Profile
[LinkedIn](https://www.linkedin.com/in/saksham-beri-32543b301/) | 
[Docker Hub](https://hub.docker.com/u/saks04)

📜 License

MIT License © 2025 Saksham Beri