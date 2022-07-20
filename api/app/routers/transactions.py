from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import APIRouter
from app.schemas import schemas
from app.routers.helpers.transactions_ops import transaction_single
from app.database.database import get_db
from datetime import date

router = APIRouter()

@router.get("/transaction/{id}", response_model=schemas.Transaction)
def get_transaction(id, db: Session = Depends(get_db)):
    return transaction_single(id, db)