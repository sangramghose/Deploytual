import pandas as pd
from sklearn.ensemble import IsolationForest
from prophet import Prophet
import matplotlib.pyplot as plt
import io, base64

def detect_anomalies(file_id: str, column: str = None) -> dict:
    """Return anomaly score per row for numeric columns."""
    df = load_dataframe(file_id)
    if column and column in df.columns:
        cols = [column]
    else:
        cols = df.select_dtypes(include='number').columns.tolist()
    if not cols:
        return {"error": "No numeric columns found."}
    
    model = IsolationForest(contamination=0.05, random_state=42)
    df_clean = df[cols].dropna()
    preds = model.fit_predict(df_clean)
    anomaly_mask = preds == -1
    anomalies = df_clean[anomaly_mask]
    return {
        "total_rows": len(df_clean),
        "anomalies_count": len(anomalies),
        "anomaly_indices": anomalies.index.tolist(),
        "anomaly_sample": anomalies.head(10).to_dict(orient='records')
    }

def generate_forecast(file_id: str, date_col: str, target_col: str, periods: int) -> dict:
    """Generate Prophet forecast and return base64 plot image + forecast data."""
    df = load_dataframe(file_id)
    # Prepare data for Prophet: ds and y
    prophet_df = df[[date_col, target_col]].copy()
    prophet_df.columns = ['ds', 'y']
    prophet_df['ds'] = pd.to_datetime(prophet_df['ds'])
    prophet_df = prophet_df.dropna()
    
    model = Prophet()
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    
    # Plot
    fig = model.plot(forecast)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    
    # Return also the forecast tail (future predictions)
    future_forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)
    return {
        "forecast_plot": f"data:image/png;base64,{img_base64}",
        "future_predictions": future_forecast.to_dict(orient='records')
    }
