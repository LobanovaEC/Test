from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app.schemas import Borrow, BorrowCreate
from app.crud import create_borrow, get_borrows, get_borrow, return_borrow
from app.database import get_db

router = APIRouter(prefix="/borrows", tags=["Borrows"])

@router.post("/", response_model=Borrow)
def create_new_borrow(borrow: BorrowCreate, db: Session = Depends(get_db)):
    try:
        return create_borrow(db, borrow)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[Borrow])
def list_borrows(db: Session = Depends(get_db)):
    return get_borrows(db)

@router.get("/{borrow_id}", response_model=Borrow)
def get_borrow_detail(borrow_id: int, db: Session = Depends(get_db)):
    borrow = get_borrow(db, borrow_id)
    if not borrow:
        raise HTTPException(status_code=404, detail="Borrow record not found")
    return borrow

@router.patch("/{borrow_id}/return", response_model=Borrow)
def return_borrow_record(borrow_id: int, return_date: date, db: Session = Depends(get_db)):
    borrow = return_borrow(db, borrow_id, return_date)
    if not borrow:
        raise HTTPException(status_code=404, detail="Borrow record not found or already returned")
    return borrow
