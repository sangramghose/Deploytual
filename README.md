# 🧠 Deploytual
### Deploy intelligence. Any data. Anywhere.

[![CI Pipeline](https://github.com/sangramghose/Deploytual/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/sangramghose/Deploytual/actions/workflows/ci.yml)
[![Docker Image](https://github.com/sangramghose/Deploytual/actions/workflows/docker.yml/badge.svg?branch=main)](https://github.com/sangramghose/Deploytual/actions/workflows/docker.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://deploytual.netlify.app)

> An AI‑powered analytics platform that unifies data connectivity, natural language querying, automated machine learning, and one‑click reporting into a single, deployable engine — ready to be dropped into any environment.

🌐 **Live Demo:** [deploytual.netlify.app](https://deploytual.netlify.app)  
📚 **API Docs:** [deploytual.onrender.com/docs](https://deploytual.onrender.com/docs)

---

## ✨ Features

- 📂 **Multi‑Source Ingestion** – CSV, Excel, PostgreSQL, MySQL, MongoDB, REST APIs  
- 🗣️ **Natural Language Querying** – Ask questions in plain English; AI converts them into SQL or Pandas  
- 🤖 **AutoML Engine** – Anomaly detection (Isolation Forest), time‑series forecasting (Prophet), and clustering  
- 🔍 **AI Data Cleaning Studio** – Missing value alerts, outlier detection, formatting issues, one‑click fixes  
- 🧠 **Explainable AI** – Every answer reveals the exact Pandas code or SQL used  
- 🔊 **AI Storyteller** – Text‑to‑speech narration with glowing animation while speaking  
- 📄 **One‑Click Executive PDF Reports** – AI‑written summaries, charts, anomaly highlights, and forecasts  
- ⚡ **Data Pipeline Builder** – Natural language or **drag‑and‑drop visual builder**; auto‑chains ETL → ML → Report  
- 📡 **Real‑Time WebSocket Notifications** – Live toasts on pipeline completion, anomaly detection, forecasts  
- 🔒 **Authentication** – Email/password sign‑up/sign‑in + Google OAuth 2.0 with JWT  
- ☸️ **Kubernetes & Helm** – Deploy to any K8s cluster with a production‑ready Helm chart  
- 🐳 **Deploy Anywhere** – Docker, Render, Netlify, GitHub Container Registry  

---

## 🛠 Tech Stack

| Layer       | Technology                                      |
|-------------|-------------------------------------------------|
| Backend     | Python, FastAPI, Pandas, NumPy                  |
| ML / AI     | scikit‑learn, Prophet                           |
| Frontend    | HTML5, CSS3, vanilla JavaScript, Chart.js (CDN) |
| Fonts       | Fraunces, Bricolage Grotesque, JetBrains Mono   |
| Databases   | MySQL, PostgreSQL, MongoDB, SQLite              |
| Auth        | JWT, Google OAuth 2.0                            |
| DevOps      | Docker, Render, Netlify, GitHub Actions, Helm   |
| Kubernetes  | Deployment, Service, Secrets, ConfigMap, Helm chart |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js (optional, for local frontend dev)
- Docker (optional)
- Google OAuth 2.0 credentials (for social login)

### Backend Setup
```bash
git clone https://github.com/sangramghose/Deploytual.git
cd Deploytual/backend
pip install -r requirements.txt
cp .env.example .env   # add your GOOGLE_CLIENT_ID and SECRET_KEY
uvicorn main:app --reload
```

Backend runs at `http://localhost:8000`  
Swagger docs: `http://localhost:8000/docs`

### Frontend Setup

The frontend is a single HTML file. Open `frontend/index.html` in a browser, or serve with:

```bash
npx serve frontend
```

When deployed, Netlify automatically serves the frontend.

### Docker

```bash
docker-compose up --build
```

### Kubernetes (with Helm)

```bash
helm install deploytual ./helm/deploytual \
  --set secrets.googleClientId=$(echo -n 'YOUR_CLIENT_ID' | base64) \
  --set secrets.secretKey=$(echo -n 'YOUR_SECRET_KEY' | base64)
```

---

## 📡 API Overview

**Base URL:** `https://deploytual.onrender.com/api`

| Method | Endpoint                     | Description                                      |
|--------|------------------------------|--------------------------------------------------|
| POST   | `/csv/upload`                | Upload CSV/Excel file                            |
| GET    | `/csv/{id}/read`             | Read dataset rows                                |
| GET    | `/csv/{id}/meta`             | Automatic profiling & statistics                 |
| POST   | `/ai/query-local`            | Natural language → Pandas analysis               |
| POST   | `/database/tables`           | List tables from a MySQL connection              |
| POST   | `/database/table/{name}`     | Fetch rows from a connected database table       |
| POST   | `/database/chat`             | Natural language query on a connected DB         |
| POST   | `/ml/anomalies`              | Detect outliers in a dataset                     |
| POST   | `/ml/forecast`               | Time‑series forecasting (Prophet)                |
| POST   | `/clean/suggest`             | Identify data quality issues                     |
| GET    | `/report/generate`           | Download a PDF executive report                  |
| POST   | `/pipeline/execute`          | Run an automated ETL‑ML‑Report pipeline          |
| POST   | `/auth/signup`               | Create account (name, email, password)           |
| POST   | `/auth/login`                | Sign in with email/password                      |
| POST   | `/auth/google`               | Sign in with Google OAuth 2.0 token              |
| WS     | `/ws`                        | Real‑time WebSocket notifications                |

Full interactive Swagger UI: [deploytual.onrender.com/docs](https://deploytual.onrender.com/docs)

---

## 🎯 Why Deploytual?

**Forward Deployed Engineers** – Drop Deploytual onto a client’s server, connect their databases, and start answering business questions immediately – with explainable AI and professional reports.

**Data Engineers** – Automated profiling, data quality checks, machine learning pipelines, forecasting – all wrapped in a portable, containerized package with Kubernetes support.

**Organizations** – Faster analytics, reduced engineering effort, AI‑powered business intelligence that runs anywhere.

---

## 📁 Project Structure

```text
Deploytual/
├── backend/
│   ├── routes/               # FastAPI routers
│   ├── services/             # Business logic
│   ├── tests/                # Pytest test suite
│   ├── config.py / main.py / schemas.py
│   ├── requirements.txt
│   └── uploads/
├── frontend/
│   └── index.html            # Complete single‑page application
├── helm/
│   └── deploytual/           # Helm chart (Kubernetes)
├── k8s/                      # Raw Kubernetes manifests
├── .github/workflows/        # CI/CD (tests, lint, security, Docker, helm-lint)
├── Makefile
├── docker-compose.yml
└── README.md
```

---

## 🔮 Roadmap

### ✅ Completed
- CSV & Excel Upload
- AI Query Engine
- Database Connectivity
- AutoML (anomaly detection & forecasting)
- AI Data Cleaning Studio
- Explainable AI
- AI Storyteller (text‑to‑speech)
- One‑Click Executive PDF Reports
- Email/password + Google OAuth Authentication
- Real‑Time WebSocket Notifications
- Kubernetes + Helm Deployment
- Drag‑and‑Drop Visual Pipeline Builder

### 🚧 In Progress
- Multi‑User Workspace & RBAC
- PostgreSQL & MongoDB direct connectors
- Real‑Time WebSocket Dashboards (beyond toasts)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

MIT © 2026 Sangram Ghose

---

## 👥 Developers

- **Sangram Ghose**  
- **Aditya Kumar Maharana**

---

🧠 **Deploy intelligence. Any data. Anywhere.**  
Built for people who hate waiting for answers.
