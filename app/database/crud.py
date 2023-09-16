from sqlalchemy.orm import Session
from datetime import date, timedelta
from . import models
from . import schemas


def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def read_contacts(db: Session, skip: int = 0, limit: int = 10, q: str = None):
    query = db.query(models.Contact)

    if q:
        query = query.filter(
            models.Contact.first_name.ilike(f"%{q}%") |
            models.Contact.last_name.ilike(f"%{q}%") |
            models.Contact.email.ilike(f"%{q}%")
        )

    return query.offset(skip).limit(limit).all()


def read_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()


def update_contact(db: Session, contact_id: int, contact: schemas.ContactUpdate):
    db_contact = db.query(models.Contact).filter(
        models.Contact.id == contact_id).first()

    if db_contact:
        for key, value in contact.dict().items():
            setattr(db_contact, key, value)

        db.commit()
        db.refresh(db_contact)

    return db_contact


def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(models.Contact).filter(
        models.Contact.id == contact_id).first()

    if db_contact:
        db.delete(db_contact)
        db.commit()

    return db_contact


def search_contacts(db: Session, query: str):
    return db.query(models.Contact).filter(
        models.Contact.first_name.ilike(f"%{query}%") |
        models.Contact.last_name.ilike(f"%{query}%") |
        models.Contact.email.ilike(f"%{query}%")
    ).all()


def get_upcoming_birthdays(db: Session, days: int):
    today = date.today()
    end_date = today + timedelta(days=days)

    return db.query(models.Contact).filter(
        models.Contact.birthdate >= today,
        models.Contact.birthdate <= end_date
    ).all()
