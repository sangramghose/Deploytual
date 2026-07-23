from fastapi import APIRouter, HTTPException
from schemas import QueryRequest, QueryResponse
from services import ai_service

router = APIRouter(prefix="/api/ai", tags=["AI"])

@router.post("/query-local", response_model=QueryResponse)
async def query_dataset_local(request: QueryRequest):
    try:
        result = ai_service.answer_question_local(
            file_id=request.file_id,
            question=request.question,
        )
        return QueryResponse(**result)
    except FileNotFoundError as e:
        raise HTTPException(404, str(e))
    except Exception as e:
        raise HTTPException(500, f"Query failed: {e}")
