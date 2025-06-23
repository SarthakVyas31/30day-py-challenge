from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

DATABASE_URL = "sqlite:///./books.db" 
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class BookDB(Base):
    __tablename__ = "books"  

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(bind=engine)

class Book(BaseModel):
    title: str
    author: str

class BookOut(Book):
    id: int

    class Config:
        orm_mode = True  


@app.get("/")
def read():
    return {"message": "Welcome to the Book Library API"}

@app.get("/books", response_model=List[BookOut])
def get_books():
    db = SessionLocal()
    books = db.query(BookDB).all()
    db.close()
    return books

@app.post("/books", response_model=BookOut)
def create_book(book: Book):
    db = SessionLocal()
    new_book = BookDB(title=book.title, author=book.author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)  
    db.close()
    return new_book

@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, updated_book: Book):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    book.title = updated_book.title
    book.author = updated_book.author
    db.commit()
    db.refresh(book)
    db.close()
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    db.delete(book)
    db.commit()
    db.close()
    return {"message": f" Book with ID {book_id} has been deleted"}
