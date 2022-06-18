from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import EmailStr
from database import get_db
import schemas
from sqlalchemy.orm import Session
import models
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.UserOut]
)
def get_all_users(db: Session = Depends(get_db), name: str = ""):
    users = db.query(models.User).\
        filter(models.User.name.like('%'+name+'%')).all()
    return users


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.UserOut
)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).\
        filter(models.User.id == id).first()
    return user


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut
)
def create_user(user: schemas.UserCreation, db: Session = Depends(get_db)):

    existing_email = db.query(models.User.email).filter_by(email=user.email).first()

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"The email already exists"
        )

    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
 