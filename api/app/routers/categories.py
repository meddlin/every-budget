from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter
from app.schemas.schemas import Category

from app.schemas import schemas
from app.routers.helpers import category_single, category_insert_single
from app.database.database import get_db

from datetime import date
from pydantic import BaseModel

router = APIRouter()


class Example(BaseModel):
    id: int
    name: str


@router.get("/category/{id}", response_model=schemas.Category)
def get_category(id, db: Session = Depends(get_db)):
    return category_single(id, db)

@router.post("/category/create")
def create_category(ex: Example, db: Session = Depends(get_db)):
    category_insert_single(db)
    return ex
    # return category_insert_single(db)

@router.post("/category/test")
def cat_test():
    return "test passed"