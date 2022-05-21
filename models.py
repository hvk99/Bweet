from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP

class Books(Base):
    __tablename__ = "books"

    bookId = Column(Integer, primary_key=True, nullable=False)
    title = Column(String)
    author = Column(String)
    avg_rating = Column(Integer)
    num_of_rating = Column(Integer)
    num_of_text_ratings = Column(Integer)
    isbn = Column(Integer)
    language = Column(String)
    num_pages = Column(Integer)
    publication_date = Column(TIMESTAMP(timezone=True))
    publisher = Column(String)
