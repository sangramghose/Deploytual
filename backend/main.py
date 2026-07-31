import os
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routes import csv_routes, ai_routes, db_routes, ml_routes, report_routes, clean_routes, auth_routes, pipeline_routes

# Ensure upload folder exists
os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)

app = FastAPI(title="Deploytual API", version="2.0.0")

# CORS: allow your frontend (Netlify)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_text(json.dumps(message))
            except Exception:
                pass

manager = ConnectionManager()

# WebSocket endpoint for real‑time updates
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Keep the connection alive by waiting for messages
            data = await websocket.receive_text()
            # You can optionally handle incoming messages here
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Include routers
app.include_router(csv_routes.router)
app.include_router(ai_routes.router)
app.include_router(db_routes.router)
app.include_router(ml_routes.router)
app.include_router(report_routes.router)
app.include_router(clean_routes.router)
app.include_router(auth_routes.router)
app.include_router(pipeline_routes.router)

@app.get("/")
def read_root():
    return {"message": "Deploytual API is running. Visit /docs for interactive API documentation."}
