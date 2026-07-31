import os
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from services.ai_service import answer_question_local
from services.ml_service import detect_anomalies, generate_forecast
from services.report_service import generate_executive_report
from services.clean_service import suggest_cleaning

@tool
def query_uploaded_data(file_id: str, question: str) -> str:
    """Answer a natural language question about an uploaded dataset (csv/excel)."""
    try:
        result = answer_question_local(file_id, question)
        code = result.get("generated_code", "")
        return f"Answer: {result['answer']}" + (f"\nPandas code used: {code}" if code else "")
    except Exception as e:
        return f"Error querying data: {e}"

@tool
def anomaly_detection(file_id: str) -> str:
    """Run anomaly detection on a dataset."""
    try:
        result = detect_anomalies(file_id)
        if "error" in result:
            return f"Anomaly detection failed: {result['error']}"
        return f"Anomalies detected: {result['anomalies_count']} out of {result['total_rows']} rows."
    except Exception as e:
        return f"Error in anomaly detection: {e}"

@tool
def time_series_forecast(file_id: str, date_col: str, target_col: str, periods: int = 30) -> str:
    """Generate a time-series forecast for a dataset. Returns summary of the forecast."""
    try:
        result = generate_forecast(file_id, date_col, target_col, periods)
        plot_available = bool(result.get("forecast_plot"))
        return f"Forecast generated for {periods} periods. Plot available: {plot_available}."
    except Exception as e:
        return f"Error generating forecast: {e}"

@tool
def data_cleaning_suggestions(file_id: str) -> str:
    """Get data quality issues and cleaning suggestions."""
    try:
        issues = suggest_cleaning(file_id)
        return str(issues)
    except Exception as e:
        return f"Error cleaning data: {e}"

@tool
def generate_pdf_report(file_id: str, title: str = "Analysis Report") -> str:
    """Generate an executive PDF report for a dataset. Returns the download URL."""
    try:
        generate_executive_report(file_id, title)
        return f"Report generated. Download it at /api/report/generate?file_id={file_id}&title={title}"
    except Exception as e:
        return f"Error generating report: {e}"

_agent = None

def get_agent():
    global _agent
    if _agent is None:
        llm = ChatGroq(
            model="llama-3.1-8b-instant",   # ✅ current free model on Groq
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY")
        )
        tools = [
            query_uploaded_data,
            anomaly_detection,
            time_series_forecast,
            data_cleaning_suggestions,
            generate_pdf_report
        ]
        _agent = create_react_agent(llm, tools)
    return _agent

def run_agent_query(user_message: str, file_id: str = None) -> str:
    agent = get_agent()
    if file_id:
        context_prompt = f" (The user is currently working with dataset ID '{file_id}'.)"
    else:
        context_prompt = ""
    inputs = {"messages": [("user", user_message + context_prompt)]}
    result = agent.invoke(inputs)
    final_msg = result["messages"][-1].content
    return final_msg
