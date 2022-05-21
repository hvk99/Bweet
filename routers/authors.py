from fastapi import APIRouter
from schemas import Book

router = APIRouter()

# Get all authors by default
#implement query parameter too
@router.get("/authors")
def add_books():
    return {
        "msg": "All authors"
    }