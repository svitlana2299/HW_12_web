from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth.models import User
from app.auth.authenticate import authenticate_user, create_user
from app.database import SessionLocal
from app.auth.jwt import Token
from app.auth.auth_utils import get_user
from pydantic import BaseModel


class RegistrationResponse(BaseModel):
    message: str = "User registered successfully"

class UserResponse(BaseModel):
    username: str
    email: str


router = APIRouter()

@router.post("/register/", response_model=UserResponse)
def register_user(user: User, db: Session = Depends(SessionLocal)):
    # Маршрут для реєстрації нового користувача
    db_user = get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return create_user(db, user)

@router.post("/login/", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(SessionLocal)):
    # Маршрут для аутентифікації та отримання JWT токену
    access_token = authenticate_user(
        db, form_data.username, form_data.password)
    if not access_token:
        raise HTTPException(status_code=401, detail="Login failed")
    return {"access_token": access_token, "token_type": "bearer"}
