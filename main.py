from fastapi import FastAPI
from routers import books, authors, users
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(books.router)
app.include_router(authors.router)
app.include_router(users.router)

@app.get(
    "/",
    response_model=None,
    summary="Checks connection",
    description="Checks initial connection",
    )
def check_setup():
    return {"msg": "success"}