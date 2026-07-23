from fastapi import APIRouter, HTTPException
from schemas import AnomalyRequest, ForecastRequest
from services import ml_service

router = APIRouter(prefix="/api/ml", tags=["ML"])

@router.post("/anomalies")
async def detect_anomalies(req: AnomalyRequest):
    try:
        result = ml_service.detect_anomalies(req.file_id, req.column)
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
        return result
    except Exception as e:
        raise HTTPException(500, f"Forecast failed: {e}")
