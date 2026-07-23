from services.csv_service import load_dataframe
import pandas as pd
import numpy as np

def suggest_cleaning(file_id: str) -> list[dict]:
    df = load_dataframe(file_id)
    issues = []
    for col in df.columns:
        nulls = df[col].isnull().sum()
        if nulls > 0:
            issues.append({
                "column": col,
                "type": "missing_values",
                "severity": "error" if nulls > len(df)*0.5 else "warning",
                "description": f"{nulls} missing values ({nulls/len(df)*100:.1f}%). Consider imputing or dropping."
            })
        if pd.api.types.is_numeric_dtype(df[col]):
            # outliers using IQR
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = df[col][(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)].count()
            if outliers > 0:
                issues.append({
                    "column": col,
                    "type": "outlier",
                    "severity": "warning",
                    "description": f"{outliers} outlier(s) detected. You may want to investigate or clip."
                })
    return issues
