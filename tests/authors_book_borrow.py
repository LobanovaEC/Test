import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_author():
    response = client.post("/authors/", json={
        "first_name": "Иван",
        "last_name": "Петров",
        "birth_date": "1988-03-01"
    })
    assert response.status_code == 200
    assert response.json()["first_name"] == "Иван"

def test_create_book():
    author_response = client.post("/authors/", json={
        "first_name": "Jane",
        "last_name": "Austen",
        "birth_date": "1775-12-16"
    })
    author_id = author_response.json()["id"]

    response = client.post("/books/", json={
        "title": "Pride and Prejudice",
        "description": "A classic novel",
        "author_id": author_id,
        "available_copies": 5
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Pride and Prejudice"


def test_borrow_book():
    author_response = client.post("/authors/", json={
        "first_name": "Emily",
        "last_name": "Bronte",
        "birth_date": "1818-07-30"
    })
    author_id = author_response.json()["id"]

    book_response = client.post("/books/", json={
        "title": "Wuthering Heights",
        "description": "A classic tale",
        "author_id": author_id,
        "available_copies": 2
    })
    book_id = book_response.json()["id"]

    borrow_response = client.post("/borrows/", json={
        "book_id": book_id,
        "reader_name": "Alice",
        "borrow_date": "2024-01-01"
    })
    assert borrow_response.status_code == 200
    assert borrow_response.json()["reader_name"] == "Alice"
    assert borrow_response.json()["book_id"] == book_id


def test_return_book():
    author_response = client.post("/authors/", json={
        "first_name": "George",
        "last_name": "Orwell",
        "birth_date": "1903-06-25"
    })
    author_id = author_response.json()["id"]

    book_response = client.post("/books/", json={
        "title": "1984",
        "description": "Dystopian novel",
        "author_id": author_id,
        "available_copies": 3
    })
    book_id = book_response.json()["id"]

    borrow_response = client.post("/borrows/", json={
        "book_id": book_id,
        "reader_name": "Bob",
        "borrow_date": "2024-01-01"
    })
    borrow_id = borrow_response.json()["id"]

    return_response = client.patch(f"/borrows/{borrow_id}/return", json={"return_date": "2024-02-01"})
    assert return_response.status_code == 200
    assert return_response.json()["return_date"] == "2024-02-01"

