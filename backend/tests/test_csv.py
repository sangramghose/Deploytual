import io
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_csv():
    file_content = "col1,col2\n1,2\n3,4"
    file = io.BytesIO(file_content.encode('utf-8'))
    response = client.post(
        "/api/csv/upload",
        files={"file": ("test.csv", file, "text/csv")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == "test.csv"
    assert data["row_count"] == 2
    assert data["column_count"] == 2
    return data["file_id"]

def test_read_csv():
    file_id = test_upload_csv()
    response = client.get(f"/api/csv/{file_id}/read?limit=10")
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 2
    assert data["columns"] == ["col1", "col2"]

def test_ai_query_local():
    file_id = test_upload_csv()
    response = client.post(
        "/api/ai/query-local",
        json={"file_id": file_id, "question": "What is the highest col1?"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "generated_code" in data   # Explainable AI
