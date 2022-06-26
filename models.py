from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Books(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    authorId = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"), nullable=False)

    author = relationship("Author")


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


class ReadList(Base):
    __tablename__ = 'userReadList'

    userId = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    bookId = Column(Integer, ForeignKey("book.id", ondelete="CASCADE"), nullable=False, primary_key=True)


class WishList(Base):
    __tablename__ = 'userWishList'

    userId = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    bookId = Column(Integer, ForeignKey("book.id", ondelete="CASCADE"), nullable=False, primary_key=True)