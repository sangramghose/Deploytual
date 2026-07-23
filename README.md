# 🧠 Deploytual

### Deploy intelligence. Any data. Anywhere.

> An AI-powered analytics platform that unifies data connectivity, natural language querying, and automated machine learning into a single, deployable engine-ready to be dropped into any environment.

---

## ✨ Features

- 📂 **Multi-Source Ingestion**
  - CSV
  - Excel
  - PostgreSQL
  - MySQL
  - MongoDB
  - REST APIs

- 🗣️ **Natural Language Querying**
  - Ask questions in plain English
  - AI automatically converts queries into SQL or Pandas operations

- 🤖 **AutoML Engine**
  - One-click anomaly detection
  - Time-series forecasting
  - Cluster analysis

- 🔍 **Instant Data Profiling**
  - Automatic schema detection
  - Missing value alerts
  - Distribution summaries
  - Data quality insights

- 📊 **Smart Visualizations**
  - Auto-generated charts
  - Export charts as PNG
  - Export processed datasets as CSV

- 🔗 **Live Dashboards**
  - Real-time analytics
  - Shareable dashboard links
  - Interactive visual reports

- 🔒 **Enterprise Security**
  - JWT Authentication
  - Role-Based Access Control (RBAC)
  - Query Audit Logs
  - Multi-Tenant Architecture

- 🐳 **Deploy Anywhere**
  - Docker support
  - Cloud deployment
  - On-premise deployment
  - Portable architecture

---

# 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python, FastAPI, Pandas, NumPy |
| **Machine Learning** | scikit-learn, Prophet |
| **AI / NLQ** | OpenAI GPT, Prompt Engineering |
| **Frontend** | React.js, Tailwind CSS, Chart.js |
| **Databases** | PostgreSQL, MySQL, MongoDB, SQLite |
| **Deployment** | Docker, Render, Vercel |

---

# 🚀 Getting Started

## Prerequisites

- Python 3.10+
- Node.js 18+
- Docker *(Optional)*
- OpenAI API Key

---

## 📦 Clone Repository

```bash
git clone https://github.com/sangramghose/Deploytual.git
cd Deploytual
```

---

# Backend Setup

```bash
cd backend

pip install -r requirements.txt

cp .env.example .env
```

Edit the `.env` file and add:

```env
OPENAI_API_KEY=your_api_key

DATABASE_URL=your_database_url
```

Run the backend:

```bash
uvicorn main:app --reload
```

Backend runs on:

```
http://localhost:8000
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# Docker Deployment

Run the complete stack:

```bash
docker-compose up --build
```

---

# 📡 API Overview

Base URL

```
/api
```

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload` | Upload CSV or Excel datasets |
| GET | `/datasets` | List all uploaded datasets |
| GET | `/datasets/{id}/meta` | Data profiling & metadata |
| POST | `/ai/query` | Ask questions in natural language |
| POST | `/ml/anomalies` | Detect anomalies |
| POST | `/ml/forecast` | Time-series forecasting |
| POST | `/ml/train` | AutoML model training |

Interactive API Documentation:

```
http://localhost:8000/docs
```

---

# 📊 Architecture

```
                +----------------------+
                |   Data Sources       |
                | CSV / SQL / MongoDB  |
                +----------+-----------+
                           |
                           ▼
                  Data Ingestion Layer
                           |
                           ▼
                 Automatic Data Profiling
                           |
                           ▼
          AI Natural Language Query Engine
                           |
             +-------------+-------------+
             |                           |
             ▼                           ▼
      Machine Learning             Visualization
      Forecasting                  Chart Generator
      Clustering                   Dashboard
      Anomaly Detection
             |
             ▼
      REST API + Dashboard
```

---

# 🖼️ Screenshots

> Replace these placeholder URLs with actual screenshots after deployment.

| Upload & Profile | AI Query | Forecast Dashboard |
|-----------------|----------|--------------------|
| https://screenshots/upload.png | https://screenshots/query.png | https://screenshots/forecast.png |

---

# 🎯 Why Deploytual?

Deploytual is built for:

### 🧑‍💻 Forward Deployed Engineers (FDE)

- Deploy directly on client infrastructure
- Connect databases in minutes
- Ask business questions immediately
- No manual SQL required

---

### 📈 Data Engineers

- Automated profiling
- Data quality monitoring
- AI-assisted analytics
- Machine learning pipelines
- Forecasting with minimal configuration

---

### 🏢 Organizations

- Faster analytics
- Better decision making
- Reduced engineering effort
- Portable deployment
- AI-powered business intelligence

---

# 📁 Project Structure

```
Deploytual/

├── backend/
│   ├── app/
│   ├── models/
│   ├── routers/
│   ├── services/
│   ├── utils/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── components/
│   ├── pages/
│   └── package.json
│
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

# 🔮 Roadmap

- [x] CSV Upload
- [x] SQL Database Integration
- [x] AI Natural Language Querying
- [x] AutoML Forecasting
- [x] Data Profiling
- [ ] PDF Report Generator
- [ ] Vector Search
- [ ] RAG Integration
- [ ] LLM Agent Workflows
- [ ] Multi-user Workspace
- [ ] Kubernetes Deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

```bash
git fork
```

2. Create a feature branch

```bash
git checkout -b feature/amazing-feature
```

3. Commit your changes

```bash
git commit -m "Add amazing feature"
```

4. Push to GitHub

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

© **2026 Sangram Ghose**

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the project
- 🐛 Report issues
- 💡 Suggest new features

---

# 📬 Contact

**Developer:** Sangram Ghose

GitHub: https://github.com/sangramghose

Repository:

https://github.com/sangramghose/Deploytual

---

## 🚀 Deploy intelligence. Any data. Anywhere.

**Build once. Deploy anywhere. Analyze everything.**
