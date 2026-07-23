import pandas as pd
from services.csv_service import load_dataframe

def answer_question_local(file_id: str, question: str) -> dict:
    """
    Local, deterministic Pandas analysis.
    Returns dict with keys: answer, insights, suggested_followups.
    """
    df = load_dataframe(file_id)
    question_lower = question.lower()

    # Initialize response
    answer = "I couldn't find a specific answer. Try asking about the data directly."
    insights = []
    followups = []

    # Determine column types
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    cat_cols = df.select_dtypes(exclude='number').columns.tolist()

    # Simple keyword-based analysis
    if "highest" in question_lower or "top" in question_lower or "max" in question_lower:
        if numeric_cols:
            col = numeric_cols[0]  # naive: pick first numeric
            max_val = df[col].max()
            row = df[df[col] == max_val].iloc[0].to_dict()
            answer = f"The highest {col} is {max_val}, found in:\n{row}"
            insights = [{"type": "highlight", "content": f"Max {col}: {max_val}"}]
        else:
            answer = "No numeric columns found to calculate highest value."
    
    elif "average" in question_lower or "mean" in question_lower:
        if numeric_cols:
            col = numeric_cols[0]
            avg = df[col].mean()
            answer = f"The average {col} is {avg:.2f}"
        else:
            answer = "No numeric columns for average calculation."

    elif "count" in question_lower and "group" in question_lower:
        if cat_cols:
            col = cat_cols[0]
            counts = df[col].value_counts().to_dict()
            answer = f"Counts for '{col}':\n" + "\n".join(f"{k}: {v}" for k,v in counts.items())
            insights = [{"type": "table", "content": counts}]
            followups.append(f"Show chart for {col} distribution")
        else:
            answer = "No categorical columns to group by."

    elif "describe" in question_lower or "summary" in question_lower:
        desc = df.describe(include='all').to_dict()
        answer = f"Here is the statistical summary:\n{desc}"
        insights = [{"type": "table", "content": desc}]

    # Generic fallback: return column info and sample
    else:
        columns_list = df.columns.tolist()
        sample = df.head(3).to_dict(orient='records')
        answer = f"The dataset has {len(df)} rows and {len(columns_list)} columns: {columns_list}. Here are the first 3 rows:\n{sample}"
        insights = [{"type": "table", "content": sample}]
    
    # Always suggest some followups
    if not followups:
        if numeric_cols:
            followups.append(f"Show me the distribution of {numeric_cols[0]}")
        if cat_cols:
            followups.append(f"Count values in {cat_cols[0]}")

    return {
        "answer": str(answer),
        "insights": insights,
        "suggested_followups": followups
    }
