import os
import uuid
import pandas as pd
from config import settings

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv', 'xlsx', 'xls'}

def save_uploaded_file(file) -> (str, str):
    """Save file, return (file_id, filepath)."""
    os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)
    file_id = str(uuid.uuid4())
    ext = file.filename.rsplit('.', 1)[1].lower()
    filename = f"{file_id}.{ext}"
    filepath = os.path.join(settings.UPLOAD_FOLDER, filename)
    with open(filepath, "wb") as f:
        f.write(file.file.read())
    return file_id, filepath

def load_dataframe(file_id: str) -> pd.DataFrame:
    """Load CSV/Excel by file_id. Raises FileNotFoundError if missing."""
    for ext in ['csv', 'xlsx', 'xls']:
        path = os.path.join(settings.UPLOAD_FOLDER, f"{file_id}.{ext}")
        if os.path.exists(path):
            if ext == 'csv':
                return pd.read_csv(path)
            else:
                return pd.read_excel(path)
    raise FileNotFoundError(f"No uploaded file found for ID {file_id}")

def get_file_metadata(file_id: str) -> dict:
    """Return basic stats about an uploaded dataset."""
    df = load_dataframe(file_id)
    path = os.path.join(settings.UPLOAD_FOLDER, f"{file_id}.csv")  # assume csv for size
    size = os.path.getsize(path) if os.path.exists(path) else 0
    return {
        "file_id": file_id,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "size_bytes": size
    }
