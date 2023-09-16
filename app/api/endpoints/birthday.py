from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import schemas, crud, models
from app.database.base import SessionLocal

router = APIRouter()


@router.get("/contacts/birthday/", response_model=list[schemas.Contact])
def get_upcoming_birthdays(days: int = 7, db: Session = Depends(SessionLocal)):
    upcoming_birthdays = crud.get_upcoming_birthdays(db, days)
    return upcoming_birthdays
