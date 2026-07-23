from fastapi import APIRouter, HTTPException
import mysql.connector
from schemas import DBConnectRequest, TableListResponse, TableDataRequest, DBChatRequest, DBChatResponse
from config import settings
import pandas as pd

router = APIRouter(prefix="/api/database", tags=["Database"])

def get_db_connection(host, port, database, user, password):
    return mysql.connector.connect(
        host=host, port=port, database=database,
        user=user, password=password
    )

@router.post("/test")
async def test_connection(req: DBConnectRequest):
    try:
        conn = get_db_connection(req.host, req.port, req.database, req.username, req.password)
        conn.close()
        return {"success": True}
    except Exception as e:
        return {"success": False, "message": str(e)}

@router.post("/tables", response_model=TableListResponse)
async def list_tables(req: DBConnectRequest):
    conn = get_db_connection(req.host, req.port, req.database, req.username, req.password)
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return {"tables": tables}

@router.post("/table/{table_name}")
async def get_table_data(table_name: str, req: TableDataRequest):
    conn = get_db_connection(req.host, req.port, req.database, req.username, req.password)
    query = f"SELECT * FROM `{table_name}` LIMIT 500"
    df = pd.read_sql(query, conn)
    conn.close()
    rows = df.fillna("").to_dict(orient='records')
    return {"rows": rows}

@router.post("/chat", response_model=DBChatResponse)
async def chat_with_database(req: DBChatRequest):
    """
    Extremely simplified chat: try to parse question and run a query.
    """
    # For now, just return a hardcoded answer; you can enhance with NL-to-SQL.
    answer = "I've executed a query based on your question, but advanced AI integration for database chat is coming soon."
    sql = "SELECT * FROM ..."  # placeholder
    return {"answer": answer, "sql": sql}
