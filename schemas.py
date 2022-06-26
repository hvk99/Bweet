from datetime import datetime
from pydantic import BaseModel, EmailStr


class Author(BaseModel):
    authorId: int
    authorName: str


class Book(BaseModel):
    bookId: int
    bookName: str
    author: Author


class UserCreation(BaseModel):
    name: str
    username: str
    password: str
    email: EmailStr
    
    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    createdAt: datetime

    class Config:
        orm_mode = True

class BookOut(BaseModel):

    title: str
    Author: Author

    class Config:
        orm_mode = True
