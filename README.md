# 🚀 KubeLink - URL Shortener Microservice (GKE + Docker + GitHub CI/CD)

KubeLink is a minimal personal mini project But production-ready URL shortener service built with Docker, Kubernetes, and deployed on Google Cloud Platform (GKE), fully automated with GitHub Actions CI/CD.

---

## 📌 Features:
- REST API for URL shortening & redirection
- PostgreSQL Database
- Dockerized for easy containerization
- Kubernetes-native deployment (GKE)
- GitHub Actions for CI/CD Pipeline
- ConfigMap & Secrets Management
- Frontend Interface (Bonus)

---

## 🏗️ Tech Stack:
- FastAPI / Node.js (Backend)
- PostgreSQL (Database)
- Docker
- Kubernetes (GKE)
- GitHub Actions (CI/CD)

---

## 🚀 Deployment Flow:
1. ✅ Push code to GitHub  
2. ✅ GitHub Actions builds Docker image & pushes it to Container Registry  
3. ✅ Deploys automatically to GKE via `kubectl`  
4. ✅ Service is available via LoadBalancer / Ingress

---

## 📂 Project Structure:
