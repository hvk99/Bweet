from pydantic import BaseModel

class Book(BaseModel):
    id: int
    name: str
    author: str
    author_id: int
    isbn: str