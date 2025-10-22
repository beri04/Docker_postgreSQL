# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Postgres client (for pg_isready)
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy wait-for-db.sh
COPY wait-for-db.sh /app/wait-for-db.sh
RUN chmod +x /app/wait-for-db.sh

# Copy app code
COPY app .
# Expose FastAPI port
EXPOSE 8000

# Default command (works even without docker-compose)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]