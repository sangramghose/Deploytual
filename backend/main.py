import os
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routes import csv_routes, ai_routes, db_routes, ml_routes, report_routes, clean_routes, auth_routes, pipeline_routes
from services.websocket_manager import manager      # 👈 import from the new module

os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)

app = FastAPI(title="Deploytual API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
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
