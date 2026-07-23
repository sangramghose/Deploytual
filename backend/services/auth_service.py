import os
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In-memory user store (replace with a real DB later)
users_db = {}

# JWT config
SECRET_KEY = os.getenv("SECRET_KEY", "deploytual-secret-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24   # 1 day

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_jwt(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def signup(name: str, email: str, password: str) -> dict:
    if email in users_db:
        raise ValueError("Email already registered")
    hashed = hash_password(password)
    users_db[email] = {
        "name": name,
        "email": email,
        "password": hashed
    }
    token = create_jwt({"sub": email, "name": name})
    return {"access_token": token, "user": {"name": name, "email": email}}

def login(email: str, password: str) -> dict:
    user = users_db.get(email)
    if not user or not verify_password(password, user["password"]):
        raise ValueError("Invalid email or password")
    token = create_jwt({"sub": email, "name": user["name"]})
    return {"access_token": token, "user": {"name": user["name"], "email": email}}

def google_login(credential: str) -> dict:
    """Verify Google ID token and return JWT."""
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    if not GOOGLE_CLIENT_ID:
        raise RuntimeError("GOOGLE_CLIENT_ID not configured")

    try:
        idinfo = id_token.verify_oauth2_token(
            credential,
            google_requests.Request(),
            GOOGLE_CLIENT_ID
        )
        email = idinfo["email"]
        name = idinfo.get("name", email)
    except Exception as e:
        raise ValueError(f"Invalid Google token: {e}")

    # Auto-register if first time
    if email not in users_db:
        users_db[email] = {
            "name": name,
            "email": email,
            "password": None   # no password for Google users
        }
    else:
        users_db[email]["name"] = name

    token = create_jwt({"sub": email, "name": name})
    return {"access_token": token, "user": {"name": name, "email": email}}
