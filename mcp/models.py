from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Book(BaseModel):
    id: int
    name: str
    type: str
    available: bool

class Order(BaseModel):
    id: str
    bookId: int
    customerName: str
    createdBy: str
    quantity: int
    timestamp: datetime

class ApiClient(BaseModel):
    clientName: str
    clientEmail: EmailStr

class ApiClientResponse(BaseModel):
    accessToken: str 