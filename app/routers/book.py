from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import Book, BookCreate
from app.crud import create_book, get_books, get_book, update_book, delete_book
from app.database import get_db

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=Book)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.get("/", response_model=list[Book])
def list_books(db: Session = Depends(get_db)):
    return get_books(db)

@router.get("/{book_id}", response_model=Book)
def get_book_detail(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=Book)
def update_book_info(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    updated_book = update_book(db, book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/{book_id}")
def delete_book_info(book_id: int, db: Session = Depends(get_db)):
    if not delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
