from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from services.clean_service import suggest_cleaning

router = APIRouter(prefix="/api/clean", tags=["Cleaning"])

class CleanRequest(BaseModel):
    file_id: str = Field(...)

class CleanIssue(BaseModel):
    column: str
    type: str          # missing_values, outlier, formatting, etc.
    severity: str      # warning, error
    description: str

class CleanResponse(BaseModel):
    file_id: str
    issues: list[CleanIssue]

@router.post("/suggest", response_model=CleanResponse)
async def suggest_cleaning(request: CleanRequest):
    try:
        issues = suggest_cleaning(request.file_id)
        return {"file_id": request.file_id, "issues": issues}
    except FileNotFoundError as e:
        raise HTTPException(404, detail=str(e))
    except Exception as e:
        raise HTTPException(500, detail=str(e))
