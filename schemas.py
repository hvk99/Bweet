import email
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
    email: EmailStr

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    createdAt: str
