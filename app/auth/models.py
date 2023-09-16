from sqlalchemy import Column, Integer, String
from app.database.base import Base
from pydantic import BaseModel

class UserResponse(BaseModel):
    username: str
    email: str


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
