from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from services.auth_service import signup, login, google_login

router = APIRouter(prefix="/api/auth", tags=["Auth"])

class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class GoogleRequest(BaseModel):
    credential: str      # the ID token from Google

class AuthResponse(BaseModel):
    access_token: str
    user: dict

@router.post("/signup", response_model=AuthResponse)
def signup_endpoint(req: SignupRequest):
    try:
        return signup(req.name, req.email, req.password)
    except ValueError as e:
        raise HTTPException(400, detail=str(e))

@router.post("/login", response_model=AuthResponse)
def login_endpoint(req: LoginRequest):
    try:
        return login(req.email, req.password)
    except ValueError as e:
        raise HTTPException(401, detail=str(e))

@router.post("/google", response_model=AuthResponse)
def google_endpoint(req: GoogleRequest):
    try:
        return google_login(req.credential)
    except ValueError as e:
        raise HTTPException(401, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(500, detail=str(e))
