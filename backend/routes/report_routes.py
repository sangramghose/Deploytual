from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse
from io import BytesIO
from services.report_service import generate_executive_report

router = APIRouter(prefix="/api/report", tags=["Report"])

@router.post("/generate")
async def generate_report(file_id: str = Query(..., description="UUID of uploaded dataset"),
                          title: str = Query("Dataset Analysis", description="Report title")):
    try:
        pdf_bytes = generate_executive_report(file_id, title)
        return StreamingResponse(
            BytesIO(pdf_bytes),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=deploytual_report_{file_id}.pdf"}
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report generation failed: {e}")
