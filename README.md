# 🧠 Deploytual

### Deploy intelligence. Any data. Anywhere.

> An AI-powered analytics platform that unifies data connectivity, natural language querying, automated machine learning, and one-click reporting into a single, deployable engine—ready to be dropped into any environment.

🌐 **Live Demo:** https://deploytual.netlify.app  
📚 **API Docs:** https://deploytual.onrender.com/docs

---

# ✨ Features

- 📂 **Multi-Source Ingestion**
  - CSV
  - Excel
  - PostgreSQL
  - MySQL
  - MongoDB
  - REST APIs
  - Upload files or connect live databases.

- 🗣️ **Natural Language Querying**
  - Ask questions in plain English.
  - AI automatically converts them into SQL or Pandas operations.

- 🤖 **AutoML Engine**
  - Anomaly Detection (Isolation Forest)
  - Time-Series Forecasting (Prophet)
  - Cluster Analysis
  - No coding required.

- 🔍 **AI Data Cleaning Studio**
  - Detect missing values
  - Find outliers
  - Identify formatting issues
  - AI-generated cleaning suggestions

- 🧠 **Explainable AI**
  - Every AI response includes the exact SQL or Pandas code used.

- 🔊 **AI Storyteller**
  - Read analysis aloud using text-to-speech.
  - Speaking text glows during narration.

- 📄 **Executive PDF Reports**
  - One-click boardroom-ready PDF reports containing:
    - Executive summary
    - Statistics
    - Forecast charts
    - Anomaly detection
    - Suggested next questions

- 📊 **Smart Visualizations**
  - Automatic charts
  - Exportable tables
  - Shareable insights

- 🔒 **Authentication**
  - Email & Password
  - Google OAuth 2.0
  - JWT Authentication

- 🐳 **Deploy Anywhere**
  - Docker
  - Render
  - Netlify
  - Runs on-premise or cloud

---

# 🛠 Tech Stack

| Layer | Technology |
|--------|------------|
| **Backend** | Python, FastAPI, Pandas, NumPy |
| **Machine Learning** | Scikit-learn, Prophet |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript, Chart.js |
| **Fonts** | Fraunces, Bricolage Grotesque, JetBrains Mono |
| **Databases** | MySQL, PostgreSQL, MongoDB, SQLite |
| **Authentication** | JWT, Google OAuth 2.0 |
| **Deployment** | Docker, Render, Netlify |

---

# 🚀 Getting Started

## Prerequisites

- Python 3.10+
- Node.js *(optional)*
- Docker *(optional)*
- Google OAuth credentials *(optional for social login)*

---

## Backend Setup

```bash
git clone https://github.com/sangramghose/Deploytual.git

cd Deploytual/backend

pip install -r requirements.txt

cp .env.example .env

# Add GOOGLE_CLIENT_ID and SECRET_KEY

uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

## Frontend Setup

The frontend is a single-page application.

Simply open:

```
frontend/index.html
```

or serve it with:

```bash
npx serve frontend
```

When deployed, Netlify automatically serves the frontend.

---

## Docker

```bash
docker-compose up --build
```

---

# 📡 API Overview

**Base URL**

```
https://deploytual.onrender.com/api
```

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/csv/upload` | Upload CSV or Excel |
| GET | `/csv/{id}/read` | Read uploaded dataset |
| GET | `/csv/{id}/meta` | Dataset profiling |
| POST | `/ai/query-local` | Natural Language → Pandas |
| POST | `/database/tables` | List database tables |
| POST | `/database/table/{name}` | Read database table |
| POST | `/database/chat` | AI SQL Chat |
| POST | `/ml/anomalies` | Detect anomalies |
| POST | `/ml/forecast` | Time-series forecasting |
| POST | `/clean/suggest` | AI data cleaning |
| GET | `/report/generate` | Generate Executive PDF |
| POST | `/auth/signup` | Register account |
| POST | `/auth/login` | Login |
| POST | `/auth/google` | Google OAuth Login |

Interactive Swagger UI:

https://deploytual.onrender.com/docs

---

# 🎯 Why Deploytual?

## 👨‍💻 Forward Deployed Engineers

Deploy Deploytual directly on a client's infrastructure, connect existing databases, and immediately start answering business questions with explainable AI and professional reports.

---

## 📊 Data Engineers

- Automated profiling
- AI-powered data cleaning
- Machine learning pipelines
- Forecasting
- Portable containerized deployment

---

## 🏢 Organizations

- Faster analytics
- Reduced engineering effort
- AI-powered Business Intelligence
- Works anywhere

---

# 📁 Project Structure

```text
Deploytual/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── config.py
│   ├── main.py
│   ├── schemas.py
│   ├── requirements.txt
│   └── uploads/
│
├── frontend/
│   └── index.html
│
├── README.md
└── .gitignore
```

---

# 🔮 Roadmap

### ✅ Completed

- CSV & Excel Upload
- AI Query Engine
- Database Connectivity
- AutoML
- AI Data Cleaning Studio
- Explainable AI
- AI Storyteller
- Executive PDF Reports
- Email Authentication
- Google OAuth

### 🚧 Planned

- PostgreSQL Connector
- MongoDB Connector
- Real-Time WebSocket Dashboards
- Drag-and-Drop Pipeline Builder
- Multi-User Workspace
- RBAC
- Kubernetes Deployment

---

# 🤝 Contributing

Contributions are always welcome!

```bash
# Fork the repository

git checkout -b feature/amazing-feature

git commit -m "Add amazing feature"

git push origin feature/amazing-feature
```

Then open a Pull Request.

---

# 📄 License

MIT License © 2026 **Sangram Ghose**

---

## 🧠 Deploy intelligence. Any data. Anywhere.

**Built for people who hate waiting for answers.**

---

**Developers:**  
- Sangram
- Aditya
  
