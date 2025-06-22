from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


books: List[Book] = []


@app.get("/")
def home():
    return {"message": "Welcome to the Library!"}


@app.get("/books")
def get_books():
    return books


@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully", "book": book}


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return {
                "message": "Book updated successfully",
                "book": updated_book
            }
    return {"error": "Book not found"}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            removed_book = books.pop(index)
            return {
                "message": "Book deleted successfully",
                "book": removed_book
            }
    return {"error": "Book not found"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
