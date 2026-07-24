from fastapi.testclient import TestClient
from main import app
from tests.test_csv import test_upload_csv

client = TestClient(app)

def test_pipeline_execute():
    file_id = test_upload_csv()
    response = client.post(
        "/api/pipeline/execute",
        json={
            "file_id": file_id,
            "instruction": "clean and detect anomalies"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["steps"]) >= 1
    assert len(data["results"]) >= 1
    for result in data["results"]:
        assert result["status"] in ("success", "error")
