from fastapi import FastAPI
from routers import books

app = FastAPI()
app.include_router(books)

@app.get(
    "/",
    response_model=None,
    summary="Checks connection",
    description="Checks initial connection",
    )
def check_setup():
    return {"msg": "success"}

# To add data about more books
@app.post("/books_csv")
def add_data(path):
    pass
