from fastapi import APIRouter, Depends, HTTPException, status, Body
from typing import List, Optional
from mcp.models import Book, Order, ApiClient, ApiClientResponse
from mcp.database import books_db, orders_db, clients_db, add_order
from mcp.auth import create_access_token, verify_token

router = APIRouter()

@router.post("/api-clients", response_model=ApiClientResponse, status_code=201)
def register_client(client: ApiClient):
    # For demo, use email as client ID
    clients_db[client.clientEmail] = client
    token = create_access_token({"sub": client.clientEmail})
    return ApiClientResponse(accessToken=token)

@router.get("/books", response_model=List[Book])
def get_books(type: Optional[str] = None):
    if type:
        return [book for book in books_db if book.type == type]
    return books_db

@router.get("/books/{bookId}", response_model=Book)
def get_book(bookId: int):
    for book in books_db:
        if book.id == bookId:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.get("/orders", response_model=List[Order])
def get_orders(user=Depends(verify_token)):
    return orders_db

@router.post("/orders", response_model=Order, status_code=201)
def create_order(
    data: dict = Body(...),
    user=Depends(verify_token)
):
    bookId = data.get("bookId")
    customerName = data.get("customerName")
    if not bookId or not customerName:
        raise HTTPException(status_code=400, detail="Missing bookId or customerName")
    order = add_order(bookId, customerName, createdBy=user["sub"], quantity=1)
    return order

@router.get("/orders/{orderId}", response_model=Order)
def get_order(orderId: str, user=Depends(verify_token)):
    for order in orders_db:
        if order.id == orderId:
            return order
    raise HTTPException(status_code=404, detail="Order not found") 