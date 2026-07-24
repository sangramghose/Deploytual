from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from services.pipeline_service import parse_pipeline_steps, execute_pipeline

router = APIRouter(prefix="/api/pipeline", tags=["Pipeline"])

class PipelineRequest(BaseModel):
    file_id: str = Field(..., description="UUID of the uploaded dataset")
    instruction: str = Field(..., description="Natural language command, e.g., 'Clean, detect anomalies, and generate PDF report'")

class StepResult(BaseModel):
    step: str
    status: str
    data: dict = {}

class PipelineResponse(BaseModel):
    steps: list[str]          # planned steps (labels)
    results: list[StepResult]  # execution results

@router.post("/execute", response_model=PipelineResponse)
async def execute_pipeline_endpoint(request: PipelineRequest):
    try:
        steps = parse_pipeline_steps(request.instruction, request.file_id)
        results = execute_pipeline(request.file_id, steps)
        return PipelineResponse(
            steps=[s["label"] for s in steps],
            results=[StepResult(**r) for r in results]
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
