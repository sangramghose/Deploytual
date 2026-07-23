from fastapi import APIRouter, UploadFile, File, HTTPException
from services import csv_service
from schemas import UploadResponse
from config import settings

router = APIRouter(prefix="/api/csv", tags=["CSV"])

@router.post("/upload", response_model=UploadResponse)
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename or not csv_service.allowed_file(file.filename):
        raise HTTPException(400, "Only CSV and Excel files are allowed.")
    file_id, path = csv_service.save_uploaded_file(file)
    df = csv_service.load_dataframe(file_id)
    return {
        "file_id": file_id,
        "filename": file.filename,
        "row_count": len(df),
        "column_count": len(df.columns)
    }

@router.get("/files")
async def list_files():
    # simple: list csv files in uploads folder (return ids)
    import os
    files = []
    for f in os.listdir(settings.UPLOAD_FOLDER):
        if f.endswith(('.csv','.xlsx','.xls')):
            files.append({"file_id": f.rsplit('.',1)[0]})
    return {"files": files}

@router.get("/{file_id}/read")
async def read_file(file_id: str, limit: int = 100):
    df = csv_service.load_dataframe(file_id)
    sample = df.head(limit).fillna("").to_dict(orient='records')
    columns = df.columns.tolist()
    return {"columns": columns, "data": sample}

@router.get("/{file_id}/meta")
async def file_meta(file_id: str):
    try:
        meta = csv_service.get_file_metadata(file_id)
        return meta
    except FileNotFoundError:
        raise HTTPException(404, "File not found")
