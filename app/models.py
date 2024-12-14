from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str]  = mapped_column(index=True)
    last_name: Mapped[str] = mapped_column(index=True)
    birth_date: Mapped[date]  = mapped_column(nullable=True)

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column()
    author_id: Mapped[str] =  mapped_column(ForeignKey("authors.id"))
    available_copies: Mapped[int] = mapped_column(default=1)

    author = relationship("Author")

class Borrow(Base):
    __tablename__ = "borrows"
    id: Mapped[int]  = mapped_column(primary_key=True, index=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    reader_name: Mapped[str] = mapped_column()
    borrow_date: Mapped[date] = mapped_column()
    return_date: Mapped[date] = mapped_column()

    book = relationship("Book")



