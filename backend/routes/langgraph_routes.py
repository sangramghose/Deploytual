from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.langgraph_agent import run_agent_query

router = APIRouter(prefix="/api/agent", tags=["Agent"])

class AgentRequest(BaseModel):
    message: str
    file_id: str | None = None

class AgentResponse(BaseModel):
    answer: str

@router.post("/query", response_model=AgentResponse)
async def agent_query(request: AgentRequest):
    try:
        answer = run_agent_query(request.message, request.file_id)
        return AgentResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
