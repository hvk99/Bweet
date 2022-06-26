from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
import schemas
from sqlalchemy.orm import Session
import models
from typing import List


router = APIRouter(
    prefix="/book",
    tags=["Book"]
)


@router.get(
    "/"
    # response_model=schemas.BookOut
)
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Books).join(models.Author).add_colums().all()
    return books

#To get a detail of a single book
@router.get("/{isbn}")
def get_books(isbn: str):
    return {
        "msg": f"Your book with ISBN: {isbn}"
    }
