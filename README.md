# TODO API – Flask + Docker

## 📌 Overview
A RESTful TODO application built using Flask, containerized with Docker, and connected to a managed PostgreSQL database.

## 🛠 Tech Stack
- Python (Flask)
- PostgreSQL (3rd-party / managed DB)
- Docker
- SQLAlchemy

## 🧱 Architecture
- Backend: Docker container
- Database: External PostgreSQL service

## 🚀 Run Locally

```bash
docker build -t todo-backend .
docker run -d \
  --env-file .env \
  -p 5000:5000 \
  todo-backend
