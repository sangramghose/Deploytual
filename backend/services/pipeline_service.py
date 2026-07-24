import logging
from services.csv_service import load_dataframe
from services.clean_service import suggest_cleaning
from services.ml_service import detect_anomalies, generate_forecast
from services.report_service import generate_executive_report

logger = logging.getLogger("deploytual.pipeline")

def parse_pipeline_steps(instruction: str, file_id: str) -> list[dict]:
    """
    Parse a natural language instruction into a list of pipeline steps.
    Returns a list of dicts with 'type' and 'label'.
    """
    steps = []
    lower = instruction.lower()
    if any(kw in lower for kw in ["clean", "scrub", "fix", "quality"]):
        steps.append({"type": "clean", "label": "Data Cleaning"})
    if any(kw in lower for kw in ["anomal", "outlier", "detect"]):
        steps.append({"type": "anomalies", "label": "Anomaly Detection"})
    if any(kw in lower for kw in ["forecast", "predict", "prophet"]):
        steps.append({"type": "forecast", "label": "Time‑Series Forecast"})
    if any(kw in lower for kw in ["report", "pdf", "summary", "executive"]):
        steps.append({"type": "report", "label": "Generate PDF Report"})
    # If nothing matches, default to a simple query summary
    if not steps:
        steps.append({"type": "query", "label": "Basic Data Summary"})
    return steps

def execute_pipeline(file_id: str, steps: list[dict]) -> list[dict]:
    """
    Execute the pipeline steps sequentially and return results.
    Each step result contains: step label, status (success/error), output data.
    """
    results = []
    # Preload dataframe to ensure file exists
    df = load_dataframe(file_id)

    for step in steps:
        try:
            if step["type"] == "clean":
                issues = suggest_cleaning(file_id)
                results.append({
                    "step": step["label"],
                    "status": "success",
                    "data": {"issues_count": len(issues), "issues": issues}
                })
            elif step["type"] == "anomalies":
                anomalies = detect_anomalies(file_id)
                results.append({
                    "step": step["label"],
                    "status": "success",
                    "data": anomalies
                })
            elif step["type"] == "forecast":
                # Need date_col and target_col – we'll pick first datetime and numeric columns
                date_col = None
                for col in df.columns:
                    if pd.api.types.is_datetime64_any_dtype(df[col]):
                        date_col = col
                        break
                if date_col is None:
                    for col in df.columns:
                        try:
                            pd.to_datetime(df[col])
                            date_col = col
                            break
                        except:
                            pass
                if date_col:
                    numeric_cols = df.select_dtypes(include='number').columns.tolist()
                    target_col = numeric_cols[0] if numeric_cols else None
                    if target_col:
                        forecast_res = generate_forecast(file_id, date_col, target_col, periods=12)
                        results.append({
                            "step": step["label"],
                            "status": "success",
                            "data": {"forecast_plot": forecast_res.get("forecast_plot")}
                        })
                    else:
                        results.append({
                            "step": step["label"],
                            "status": "error",
                            "data": {"error": "No numeric target column found for forecasting."}
                        })
                else:
                    results.append({
                        "step": step["label"],
                        "status": "error",
                        "data": {"error": "No date column detected for forecasting."}
                    })
            elif step["type"] == "report":
                pdf_bytes = generate_executive_report(file_id, title="Pipeline Report")
                results.append({
                    "step": step["label"],
                    "status": "success",
                    "data": {"report_ready": True}
                })
            elif step["type"] == "query":
                # Use ai_service to answer a default question
                from services.ai_service import answer_question_local
                answer = answer_question_local(file_id, "Give me a summary of this dataset.")
                results.append({
                    "step": step["label"],
                    "status": "success",
                    "data": answer
                })
        except Exception as e:
            logger.error(f"Pipeline step {step['label']} failed: {e}")
            results.append({
                "step": step["label"],
                "status": "error",
                "data": {"error": str(e)}
            })
    return results
