from fastapi import FastAPI
from app.api.endpoints import contact, birthday
from .auth.main import app as auth_app
from .api.endpoints import router as api_router

app = FastAPI()

app.include_router(contact.router, prefix="/api/v1")
app.include_router(birthday.router, prefix="/api/v1")
app.include_router(auth_app, prefix="/auth")
app.include_router(api_router, prefix="/api")
