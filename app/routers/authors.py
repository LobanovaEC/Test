from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import Author, AuthorCreate
from app.crud import create_author, get_authors, get_author, update_author, delete_author
from app.database import get_db

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.post("/", response_model=Author)
def create_new_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db, author)

@router.get("/", response_model=list[Author])
def list_authors(db: Session = Depends(get_db)):
    return get_authors(db)

@router.get("/{author_id}", response_model=Author)
def get_author_detail(author_id: int, db: Session = Depends(get_db)):
    author = get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.put("/{author_id}", response_model=Author)
def update_author_info(author_id: int, author: AuthorCreate, db: Session = Depends(get_db)):
    updated_author = update_author(db, author_id, author)
    if not updated_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated_author

@router.delete("/{author_id}")
def delete_author_info(author_id: int, db: Session = Depends(get_db)):
    if not delete_author(db, author_id):
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}
