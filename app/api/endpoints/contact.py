from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import schemas, crud, models
from app.database.base import SessionLocal

router = APIRouter()


@router.post("/contacts/", response_model=schemas.Contact)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(SessionLocal)):
    db_contact = crud.create_contact(db, contact)
    return db_contact


@router.get("/contacts/", response_model=list[schemas.Contact])
def read_contacts(skip: int = Query(0, alias="page", description="Skip results"),
                  limit: int = Query(10, description="Limit results"),
                  q: str = Query(None, description="Search query"),
                  db: Session = Depends(SessionLocal)):
    pass


@router.get("/contacts/{contact_id}", response_model=schemas.Contact)
def read_contact(contact_id: int, db: Session = Depends(SessionLocal)):
    db_contact = crud.read_contact(db, contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact


@router.put("/contacts/{contact_id}", response_model=schemas.Contact)
def update_contact(contact_id: int, contact: schemas.ContactUpdate, db: Session = Depends(SessionLocal)):
    db_contact = crud.update_contact(db, contact_id, contact)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact


@router.delete("/contacts/{contact_id}", response_model=dict)
def delete_contact(contact_id: int, db: Session = Depends(SessionLocal)):
    db_contact = crud.delete_contact(db, contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {}


@router.get("/contacts/", response_model=list[schemas.Contact])
def read_contacts(skip: int = Query(0, alias="page", description="Skip results"),
                  limit: int = Query(10, description="Limit results"),
                  q: str = Query(None, description="Search query"),
                  db: Session = Depends(SessionLocal)):
    contacts = crud.read_contacts(db, skip=skip, limit=limit, q=q)
    return contacts
