from fastapi import APIRouter, Depends, status
from database import get_db
import schemas
from sqlalchemy.orm import Session
import models

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/current")
def get_current_user():
    return "Books added successfully"


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED
)
def create_user(user: schemas.UserCreation, db: Session = Depends(get_db)):

    ## add logic here to only allow unique email

    new_user = models.User(
        name=user.name,
        email=user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
