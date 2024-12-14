from fastapi import FastAPI
from app.routers import authors, books, borrows

app = FastAPI()

# Подключение роутеров
app.include_router(authors.router)
app.include_router(books.router)
app.include_router(borrows.router)
