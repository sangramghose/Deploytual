from pydantic import BaseModel
from typing import List, Optional, Any

# --- CSV Upload ---
class UploadResponse(BaseModel):
    file_id: str
    filename: str
    row_count: int
    column_count: int

# --- AI / Query ---
class QueryRequest(BaseModel):
    file_id: str
    question: str
    max_rows: int = 500

class InsightItem(BaseModel):
    type: str
    content: Any

class QueryResponse(BaseModel):
    answer: str
    insights: List[InsightItem] = []
    suggested_followups: List[str] = []

# --- Database ---
class DBConnectRequest(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str

class TableListResponse(BaseModel):
    tables: List[str]

class TableDataRequest(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str

class DBChatRequest(BaseModel):
    question: str

class DBChatResponse(BaseModel):
    answer: str
    sql: Optional[str] = None

# --- ML ---
class AnomalyRequest(BaseModel):
    file_id: str
    column: Optional[str] = None   # if not given, detect on all numeric columns

class ForecastRequest(BaseModel):
    file_id: str
    date_col: str
    target_col: str
    periods: int = 30

class TrainRequest(BaseModel):
    file_id: str
    target_col: str
    features: Optional[List[str]] = None  # optional, else all numeric except target
