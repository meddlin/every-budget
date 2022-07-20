import datetime
from typing import List
import uuid
from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter
from app.schemas.budget import Budget, PartialBudget
from app.routers.helpers.budget_ops import budget_single, budget_create, budget_update, budget_delete, budget_get_all
from app.database.database import get_db

from datetime import date

router = APIRouter()

###
# Retrieve data for a single Budget object
@router.get("/budget/{id}", response_model=Budget)
def get_budget(id, db: Session = Depends(get_db)):
    return budget_single(id, db)


@router.post("/budget/get_all", response_model = List[Budget])
def get_all_budgets(db: Session = Depends(get_db)):
    return budget_get_all(db)

###
# Creates a new Budget model
# - Upon successful creation this should return a "success" message,
#   and the resulting Budget object data
@router.put("/budget/create", response_model=Budget)
def create_budget(db: Session = Depends(get_db)):
    return budget_create(db)

###
# Partial update for the Budget model
# - Return if update is successful
@router.patch("/budget/update", response_model=PartialBudget)
def update_budget(partial_budget: PartialBudget, db:Session = Depends(get_db)):
    return budget_update(partial_budget, db)

###
# Delete a budget record from the database
@router.delete("/budget/delete/{id}")
def delete_budget(id, db: Session = Depends(get_db)):
    return budget_delete(id, db)