from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Contact Book API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Contact Book API"}

@app.post("/contacts/", response_model=schemas.Contact, status_code=201, summary="Create a new contact")
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    """
    Create a new contact with the following information:
    
    - **name**: Name of the contact (required)
    - **address**: Address of the contact (required)
    - **phone**: Phone number (optional)
    - **email**: Email address (optional)
    """
    return crud.create_contact(db=db, contact=contact)

@app.get("/contacts/", response_model=List[schemas.Contact], summary="Get all contacts")
def read_contacts(skip: int = Query(0, description="Skip N contacts"), 
                  limit: int = Query(100, description="Limit the number of contacts returned"),
                  db: Session = Depends(get_db)):
    """
    Retrieve all contacts with pagination support.
    """
    contacts = crud.get_contacts(db, skip=skip, limit=limit)
    return contacts

@app.get("/contacts/{contact_id}", response_model=schemas.Contact, summary="Get a specific contact")
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific contact by ID.
    """
    db_contact = crud.get_contact(db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@app.put("/contacts/{contact_id}", response_model=schemas.Contact, summary="Update a contact")
def update_contact(contact_id: int, contact: schemas.ContactUpdate, db: Session = Depends(get_db)):
    """
    Update an existing contact.
    """
    return crud.update_contact(db=db, contact_id=contact_id, contact=contact)

@app.delete("/contacts/{contact_id}", response_model=schemas.Contact, summary="Delete a contact")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    """
    Delete a contact by ID.
    """
    return crud.delete_contact(db=db, contact_id=contact_id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
