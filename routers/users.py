from fastapi import APIRouter
from schemas import Book

router = APIRouter()

@router.post("/add_books")
def add_books():
    return {
        "msg": "Books added successfully"
    }
