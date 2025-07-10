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
- FastAPI (Backend)
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
KubeLink---URL-Shortener-Service/
│
├── api/                           # FastAPI Backend App
│   ├── main.py                    # App entry point
│   ├── database.py                # Database connection config
│   ├── models.py                  # SQLAlchemy models
│   ├── schemas.py                 # Pydantic schemas
│   ├── crud.py                    # Database CRUD operations
│   └── requirements.txt           # Python dependencies
│
├── k8s/                           # Kubernetes Manifests
│   ├── deployment.yaml            # API Deployment
│   ├── service.yaml               # API Service
│   ├── configmap.yaml             # ConfigMaps (App settings)
│   ├── secret.yaml                # Secrets (DB credentials)
│   └── ingress.yaml               # Ingress (optional, for custom domain / HTTPS)
│
├── .github/                       # GitHub Actions CI/CD Pipeline
│   └── workflows/
│       └── deploy.yml             # CI/CD workflow for build & deploy
│
├── Dockerfile                     # Dockerfile for backend container
├── docker-compose.yml             # Docker Compose (Local Dev)
├── README.md                      # Project Documentation
└── LICENSE                        # License (MIT)

