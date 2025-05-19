from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class ContactBase(BaseModel):
    name: str
    address: str
    phone: Optional[str] = None
    email: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class Contact(ContactBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
