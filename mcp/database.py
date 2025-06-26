from typing import List, Dict
from mcp.models import Book, Order, ApiClient
from datetime import datetime
import uuid

books_db: List[Book] = [
    Book(id=1, name="The Great Gatsby", type="fiction", available=True),
    Book(id=2, name="A Brief History of Time", type="non-fiction", available=True),
]

orders_db: List[Order] = []
clients_db: Dict[str, ApiClient] = {}

def add_order(bookId: int, customerName: str, createdBy: str, quantity: int = 1) -> Order:
    order = Order(
        id=str(uuid.uuid4()),
        bookId=bookId,
        customerName=customerName,
        createdBy=createdBy,
        quantity=quantity,
        timestamp=datetime.utcnow(),
    )
    orders_db.append(order)
    return order 