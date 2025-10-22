🧾 POSTMORTEM REPORT – FastAPI + PostgreSQL + Docker Setup

Date: 21 October 2025
Author: Saksham Beri
Environment: Docker + WSL2 + FastAPI + PostgreSQL + pgAdmin
Objective: Build a containerized FastAPI app connected to PostgreSQL with persistence and external DB access (pgAdmin).

🧩 1. Summary

The goal was to containerize a FastAPI backend with PostgreSQL, ensuring:

Database runs independently via Docker.

FastAPI connects automatically on startup.

Data persists through volumes.

Connection verified using both API routes and pgAdmin.

After multiple iterations, the system successfully connected and stored data end-to-end:
FastAPI → psycopg2 → PostgreSQL (Docker) → pgAdmin (GUI verification).

# 🧠 2. Problem Timeline & Resolutions
  - Stage	Error/Issue	Root Cause	Solution Implemented	Skill Learned
    🧱 Environment Setup	docker-compose not found in WSL	Docker Desktop not integrated with WSL2	Enabled WSL integration in Docker Desktop	Proper environment linking between Windows & Linux subsystems
    🧱 YAML Validation	empty compose file / ports must be array	YAML formatting errors	Fixed indentation + removed deprecated version	Docker Compose file syntax & validation
    🧱 Dockerfile Build	invalid reference format: baseImage	Incorrect naming / path errors	Lowercased names & corrected build context	Docker build contexts & naming conventions
🧱 Script Not Found	./wait-for-db.sh: no such file	File not copied into container	Added COPY wait-for-db.sh /app/ in Dockerfile	File path management in images
🧱 Missing Command	pg_isready: not found	PostgreSQL client not installed in Python image	Installed using apt-get install postgresql-client	Slim image dependency installation
🧱 Connection Refused	FastAPI started before DB ready	Race condition in startup order	Implemented wait-for-db.sh retry logic	Service orchestration in Docker
🧱 Volume Conflict	Database directory appears to contain a database	Persistent volume reused between builds	Cleaned volumes using docker compose down -v	Data persistence management
🧱 pgAdmin Connection	Table not visible	Connected to local Postgres instead of container DB	Stopped local service & reconnected to Docker	Network isolation & host conflict resolution
# ⚙️ 3. Root Causes Explained in Depth
1️⃣ Startup Race Condition

FastAPI container booted faster than PostgreSQL → connection refused.
Fix: Added a wait script:

until pg_isready -h db -U postgres; do
  echo "Postgres is unavailable - waiting"
  sleep 2
done

2️⃣ Build Context Isolation

Files in parent directories (like wait-for-db.sh) weren’t copied into the container.
Fix: Ensured project structure like:

📦 API's/
 ┣ 📂 app/
 ┣ 📜 Dockerfile
 ┣ 📜 docker-compose.yml
 ┣ 📜 wait-for-db.sh

3️⃣ Local vs Docker DB Conflict

pgAdmin connected to local Windows DB (port 5432) instead of container DB.
Fix: Stopped local DB service → pgAdmin connected to Docker container successfully.

📘 4. Technical Verification Logs

FastAPI Logs:

Connected to: ('PostgreSQL 15.x on x86_64-pc-linux-gnu...')
INFO: Application startup complete.


PostgreSQL Logs:

database system is ready to accept connections


Database Validation:

postgres=# SELECT * FROM notes;
 id |  title  |  content
----+---------+-----------
  1 | Saksham | yoyoyoyoyo
(1 row)


✅ Verified successful data persistence and container synchronization.

🧰 5. Final Working Stack Overview
Component	Description
FastAPI (app)	Handles routes & inserts notes into PostgreSQL
PostgreSQL (db)	Stores persistent note data
pgAdmin	GUI for DB verification
Docker Compose	Orchestrates both services
wait-for-db.sh	Ensures DB readiness before FastAPI starts
Volume	Persists PostgreSQL data across container restarts
🧭 6. Final System Architecture
 ┌──────────────────┐
 │     FastAPI      │
 │  (Python + Psyco)│
 └─────────┬────────┘
           │  (SQL Query)
           ▼
 ┌──────────────────┐
 │   PostgreSQL DB  │
 │ (Docker Service) │
 └─────────┬────────┘
           │  (Data Verification)
           ▼
 ┌──────────────────┐
 │     pgAdmin      │
 │  (External GUI)  │
 └──────────────────┘

🚀 7. Outcome

✅ Containers build and run via docker compose up
✅ FastAPI automatically connects to PostgreSQL
✅ Table notes created automatically
✅ Data persisted and verified in pgAdmin

This marks Saksham Beri’s first full production-grade backend environment setup — including CI/CD-style orchestration concepts used by Jenkins/Apache Infra teams.

🧠 8. Key Learnings Summary
Category	Takeaway
Docker	Mastered multi-container orchestration
Networking	Learned host/port mapping and service linking
DBMS	Practically implemented schema creation and data persistence
Debugging	Developed habit of analyzing multi-level logs
CI/CD Preparation	Built foundations identical to real-world pipelines (DB wait, Docker build, health checks)
💬 9. Conclusion

This project was not just about connecting FastAPI with PostgreSQL —
it was about understanding the invisible system design layer behind every production backend.

Every problem solved here (from WSL integration to DB race conditions) mirrors what real DevOps engineers deal with daily at Jenkins, Apache, and AWS.
This marks the transition from student developer → backend engineer mindset.