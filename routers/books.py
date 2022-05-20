from fastapi import APIRouter
from schemas import Book

router = APIRouter()

@router.post("/add_books")
def add_books():
    return {
        "msg": "Books added successfully"
    }

# Get a list of applicable books
# implement query parameter too 
@router.get("/books/")
def get_books():
    return {
        "msg": "All Books"
    }

#To get a detail of a single book
@router.get("/books/{isbn}")
def get_books(isbn: str):
    return {
        "msg": "All Books"
    }


# Get all authors by default
#implement query parameter too
@router.get("/authors")
def add_books():
    return {
        "msg": "All authors"
    }