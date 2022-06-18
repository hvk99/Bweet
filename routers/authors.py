from fastapi import APIRouter
from schemas import Author


router = APIRouter(
    prefix="/author",
    tags=["Author"]
)


@router.get("/")
def get_authors():
    return {
        "msg": "All authors"
    }