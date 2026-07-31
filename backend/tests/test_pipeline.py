import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import io
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_pipeline_execute():
    # 1. Upload a CSV directly
    file_content = "col1,col2\n1,2\n3,4"
    file = io.BytesIO(file_content.encode('utf-8'))
    upload_response = client.post(
        "/api/csv/upload",
        files={"file": ("test.csv", file, "text/csv")}
    )
    assert upload_response.status_code == 200
    upload_data = upload_response.json()
    file_id = upload_data["file_id"]

    # 2. Execute the pipeline
    response = client.post(
        "/api/pipeline/execute",
        json={
            "file_id": file_id,
            "instruction": "clean and detect anomalies"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "steps" in data
    assert "results" in data
    assert len(data["steps"]) >= 1
    for result in data["results"]:
        assert result["status"] in ("success", "error")
