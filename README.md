# FastAPI CI/CD Pipeline on AWS EC2

Automated CI/CD pipeline built with Jenkins, Docker, and AWS EC2, deploying a FastAPI + PostgreSQL backend.
Every push to GitHub triggers Jenkins → builds Docker image → scans → pushes to Docker Hub → deploys containerized app automatically.

# 🧩 Architecture Overview
![alt text](<image.png>)


# 🛠️ Tech Stack

<table>
  <thead style="background-color:#2e2e2e;color:white;">
    <tr>
      <th>Layer</th>
      <th>Tools Used</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Cloud & Infra</td><td>AWS EC2, Docker Engine</td></tr>
    <tr><td>CI/CD</td><td>Jenkins (Declarative Pipeline)</td></tr>
    <tr><td>Backend</td><td>FastAPI, Swagger UI</td></tr>
    <tr><td>Database</td><td>PostgreSQL</td></tr>
    <tr><td>Container Registry</td><td>Docker Hub</td></tr>
    <tr><td>Code Repo</td><td>GitHub (Webhook Trigger)</td></tr>
  </tbody>
</table>


# ⚙️ Pipeline Flow
```
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
```

# 🧾 Project Structure
```
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
```
# 🚀 Deployment Steps (Short)
**1. Clone repo**
```
git clone https://github.com/beri04/Docker_postgreSQL
```

**2. Build and run locally (optional)**
```docker-compose up --build```
           **or**
```docker compose up --build```

**3. CI/CD handled by Jenkins on EC2**
    → Pulls latest code
    → Builds Docker image
    → Pushes to Docker Hub
    → Deploys FastAPI + PostgreSQL containers

# 🧠 Key Learnings
  → End-to-end DevOps automation using Jenkins Declarative Pipeline
  → Multi-container orchestration via Docker Compose
  → Secure database connection inside private Docker network
  → AWS EC2 as a persistent host for Jenkins and FastAPI services
  → Real-world debugging of build failures, Docker credential issues, and webhooks


# 🏷️ Badges
[![Docker Image](https://img.shields.io/badge/DockerHub-saks04%2Ffastapi--backend-blue?logo=docker)](https://hub.docker.com/r/saks04/fastapi-backend)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Automated-blue?logo=docker)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green?logo=fastapi)
![AWS](https://img.shields.io/badge/Deployed_on-AWS-orange?logo=amazon-aws)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue?logo=postgresql)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?logo=python)


# 🧑‍💻 Author
Saksham Beri
Backend & DevOps Engineer | FastAPI • Docker • Jenkins • AWS

**🔗 Profile**

[LinkedIn](https://www.linkedin.com/in/saksham-beri-32543b301/) | 
[Docker Hub](https://hub.docker.com/u/saks04)

# 📜 License

MIT License © 2025 Saksham Beri