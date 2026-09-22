import os
import pandas as pd
from services.csv_service import load_dataframe
from services.ai_service import answer_question_local

def _make_csv(tmp_path):
    csv_path = tmp_path / "sample.csv"
    pd.DataFrame({
        "category": ["A", "B", "A", "B"],
        "sales": [10, 200, 50, 100],
        "age": [20, 30, 40, 50],
    }).to_csv(csv_path, index=False)
    return csv_path

def test_highest_named_column(tmp_path, monkeypatch):
    csv_path = _make_csv(tmp_path)
    # csv_service builds the upload path from settings.UPLOAD_FOLDER.
    from config import settings
    os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)
    target = os.path.join(settings.UPLOAD_FOLDER, "regression_sample.csv")
    pd.read_csv(csv_path).to_csv(target, index=False)

    result = answer_question_local("regression_sample", "What is the highest sales?")
    assert result["answer"].startswith("The highest sales is 200")
    assert "sales" in result["generated_code"]

def test_average_named_column(tmp_path):
    from config import settings
    os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)
    target = os.path.join(settings.UPLOAD_FOLDER, "regression_average.csv")
    pd.DataFrame({"category": ["A", "B"], "sales": [10, 30], "age": [20, 40]}).to_csv(target, index=False)

    result = answer_question_local("regression_average", "What is the average sales?")
    assert result["answer"].startswith("The average sales is 20.00")
