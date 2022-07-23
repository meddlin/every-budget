from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import APIRouter
from app.schemas.transaction import Transaction, PartialTransaction
from app.routers.helpers.transactions_ops import transaction_single, transactions_get_all, transaction_create, transaction_update, transaction_delete
from app.database.database import get_db
from datetime import date

router = APIRouter()

@router.get("/transaction/{id}", response_model=Transaction)
def get_transaction(id, db: Session = Depends(get_db)):
    return transaction_single(id, db)

@router.post("/transaction/get_all", response_model = List[Transaction])
def get_all_transactions(db: Session = Depends(get_db)):
    return transactions_get_all(db)

@router.put("/transaction/create", response_model=Transaction)
def create_transaction(db: Session = Depends(get_db)):
    return transaction_create(db)

@router.patch("/transaction/patch", response_model=PartialTransaction)
def update_transaction(partial: PartialTransaction, db: Session = Depends(get_db)):
    return transaction_update(partial, db)

@router.delete("/transaction/delete/{id}")
def delete_transaction(id, db: Session = Depends(get_db)):
    return transaction_delete(id, db)