from fastapi import APIRouter, HTTPException
from schemas import AnomalyRequest, ForecastRequest
from services import ml_service
from main import manager           # 👈 WebSocket manager
import datetime                     # 👈 for timestamp

router = APIRouter(prefix="/api/ml", tags=["ML"])

@router.post("/anomalies")
async def detect_anomalies(req: AnomalyRequest):
    try:
        result = ml_service.detect_anomalies(req.file_id, req.column)
        # Broadcast to all connected clients
        await manager.broadcast({
            "event": "anomaly_detection_completed",
            "file_id": req.file_id,
            "anomalies_count": result.get("anomalies_count", 0),
            "total_rows": result.get("total_rows", 0),
            "timestamp": datetime.datetime.utcnow().isoformat()
        })
        return result
    except FileNotFoundError as e:
        raise HTTPException(404, str(e))
    except Exception as e:
        raise HTTPException(500, f"Anomaly detection failed: {e}")

@router.post("/forecast")
async def forecast(req: ForecastRequest):
    try:
        result = ml_service.generate_forecast(
            req.file_id, req.date_col, req.target_col, req.periods
        )
        # Broadcast forecast completion
        await manager.broadcast({
            "event": "forecast_completed",
            "file_id": req.file_id,
            "target": req.target_col,
            "periods": req.periods,
            "timestamp": datetime.datetime.utcnow().isoformat()
        })
        return result
    except Exception as e:
        raise HTTPException(500, f"Forecast failed: {e}")
