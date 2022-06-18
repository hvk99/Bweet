from fastapi import APIRouter, HTTPException, Response, status
from schemas import Book
from typing import List
import pandas as pd

router = APIRouter(
    prefix="/book",
    tags=["Book"]
)

# This will be used to add more books to the database
@router.post(
    "/add_books/",
    response_model=List[Book])
def add_books():

    path = r"Some directory/some excel"
    pd.read_csv(path)

    # if path == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"The path sent does not exist")

    return {"msg": "Books added successfully"}

# Get a list of applicable books
# implement query parameter too 
@router.get("/")
def get_books():
    return {
        "msg": "All Books"
    }

#To get a detail of a single book
@router.get("/{isbn}")
def get_books(isbn: str):
    return {
        "msg": f"Your book with ISBN: {isbn}"
    }
