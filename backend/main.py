import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routes import csv_routes, ai_routes, db_routes, ml_routes

# Ensure upload folder exists
os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)

app = FastAPI(title="Deploytual API", version="1.0.0")

# CORS: allow your frontend (Netlify/Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(csv_routes.router)
app.include_router(ai_routes.router)
app.include_router(db_routes.router)
app.include_router(ml_routes.router)

@app.get("/")
def read_root():
    return {"message": "Deploytual API is running. Visit /docs for interactive API documentation."}
