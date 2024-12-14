from sqlalchemy.orm import Session
from app.models import Author, Book, Borrow

# CRUD для авторов
def create_author(db: Session, author_data):
    author = Author(**author_data.dict())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def get_authors(db: Session):
    return db.query(Author).all()

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def update_author(db: Session, author_id: int, author_data):
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        for key, value in author_data.dict(exclude_unset=True).items():
            setattr(author, key, value)
        db.commit()
        db.refresh(author)
    return author

def delete_author(db: Session, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        db.delete(author)
        db.commit()
    return author



def create_book(db: Session, book_data):
    book = Book(**book_data.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books(db: Session):
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db: Session, book_id: int, book_data):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        for key, value in book_data.dict(exclude_unset=True).items():
            setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book




def create_borrow(db: Session, borrow_data):

    book = db.query(Book).filter(Book.id == borrow_data.book_id).first()
    if not book or book.available_copies <= 0:
        raise ValueError("Book is not available for borrowing.")


    book.available_copies -= 1
    db.add(book)


    borrow = Borrow(**borrow_data.dict())
    db.add(borrow)
    db.commit()
    db.refresh(borrow)
    return borrow



def get_borrows(db: Session):
    return db.query(Borrow).all()



def get_borrow(db: Session, borrow_id: int):
    return db.query(Borrow).filter(Borrow.id == borrow_id).first()



def return_borrow(db: Session, borrow_id: int, return_date):
    borrow = db.query(Borrow).filter(Borrow.id == borrow_id).first()
    if borrow and not borrow.return_date:

        borrow.return_date = return_date


        book = db.query(Book).filter(Book.id == borrow.book_id).first()
        if book:
            book.available_copies += 1
            db.add(book)

        db.commit()
        db.refresh(borrow)
    return borrow
