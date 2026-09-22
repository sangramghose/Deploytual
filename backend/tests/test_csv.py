import io
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_ai_query_local():
    # 1. Upload a CSV
    file_content = "col1,col2\n1,2\n3,4"
    file = io.BytesIO(file_content.encode("utf-8"))

    upload_response = client.post(
        "/api/csv/upload",
        files={"file": ("test.csv", file, "text/csv")}
    )

    assert upload_response.status_code == 200

    upload_data = upload_response.json()
    file_id = upload_data["file_id"]

    # 2. Ask the local AI query endpoint
    response = client.post(
        "/api/ai/query-local",
        json={
            "file_id": file_id,
            "question": "What is the highest col1?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "generated_code" in data