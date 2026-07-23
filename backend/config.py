import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    UPLOAD_FOLDER = "uploads"
    MAX_UPLOAD_SIZE_MB = 500
    MAX_ROWS_FOR_AI = 100   # for local Pandas analysis, limit rows for safety
    # Database defaults (can be overridden by env)
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "datamind")

settings = Settings()
