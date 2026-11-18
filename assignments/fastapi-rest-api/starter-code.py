from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Frankenstein", "author": "Mary Shelley"},
]


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


@app.get("/books")
def list_books():
    return books


@app.post("/books", status_code=201)
def create_book(book: BookInput):
    raise NotImplementedError("Implement POST /books")


@app.get("/books/{book_id}")
def get_book(book_id: int):
    raise NotImplementedError("Implement GET /books/{book_id}")


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    raise NotImplementedError("Implement PUT /books/{book_id}")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    raise NotImplementedError("Implement DELETE /books/{book_id}")
