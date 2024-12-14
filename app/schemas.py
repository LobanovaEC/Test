from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    description: str
    author_id: int
    available_copies: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class BorrowBase(BaseModel):
    book_id: int
    reader_name: str
    borrow_date: date

class BorrowCreate(BorrowBase):
    pass

class Borrow(BorrowBase):
    id: int
    return_date: Optional[date] = None

    class Config:
        orm_mode = True
