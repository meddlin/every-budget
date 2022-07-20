from typing import List
from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter
from app.schemas.category import PartialCategory

from app.schemas.category import Category
from app.routers.helpers.categories_ops import categories_get_all, category_single, category_insert_single, category_update, category_delete
from app.database.database import get_db

from datetime import date
from pydantic import BaseModel
import uuid

router = APIRouter()

@router.get("/category/{id}", response_model=Category)
def get_category(id, db: Session = Depends(get_db)):
    return category_single(id, db)

@router.post("/category/get_all", response_model = List[Category])
def get_all_categories(db: Session = Depends(get_db)):
    return categories_get_all(db)

@router.post("/category/create")
def create_category(db: Session = Depends(get_db)):
    category_insert_single(db)
    return "check this method"
    # return category_insert_single(db)

@router.patch("/category/patch", response_model=PartialCategory)
def update_category(partial: PartialCategory, db: Session = Depends(get_db)):
    return category_update(partial, db)

@router.delete("/category/delete/{id}")
def delete_category(id, db: Session = Depends(get_db)):
    return category_delete(id, db)