from dataclasses import dataclass, field, asdict
import re

@dataclass
class Library:
    Title: str
    Author: str
    ISBN: int
    Publication_Year: int

    def Display(self):
        print(asdict(self))


def user_Input():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    while True: 
        isbn = input("Enter Book ISBN Number: ")
        if re.fullmatch(r"\d{13}", isbn):
            ISBN = int(isbn)
            break
        else:
            print("Enter Valid !3digit ISBN Number")

    publication_year = int(input("Enter Publication Year of Book: "))
    return Library(title, author, ISBN, publication_year)

def perform():
    Books = []
    while True:
        Book = user_Input()
        Books.append(Book)

        multiple = input("Do you want to add another book?(yes/no):")
        
        if multiple!= "Yes":
            break
    
    print("Books in Library:")

    for index, Book in enumerate(Books, 1):
        print(f"Book {index}:")
        Book.Display()


if __name__ == "__main__":
        perform()
