import datetime
import uuid
from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter

from app.schemas import schemas
from app.routers.helpers import budget_single
from app.database.database import get_db

from datetime import date

router = APIRouter()

@router.get("/budget/{id}", response_model=schemas.Budget)
def get_budget(id, db: Session = Depends(get_db)):
    return budget_single(id, db)