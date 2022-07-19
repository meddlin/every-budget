import datetime
from typing import List
import uuid
from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter
from app.schemas.schemas import PartialBudget

from app.schemas import schemas
from app.routers.helpers import budget_single, budget_create, budget_update, budget_delete, budget_get_all
from app.database.database import get_db

from datetime import date

router = APIRouter()

@router.get("/budget")
def test_budget():
    return "test"

###
# Retrieve data for a single Budget object
@router.get("/budget/{id}", response_model=schemas.Budget)
def get_budget(id, db: Session = Depends(get_db)):
    return budget_single(id, db)


@router.post("/budget/get_all", response_model = List[schemas.Budget])
def get_all_budgets(db: Session = Depends(get_db)):
    return budget_get_all(db)

###
# Creates a new Budget model
# - Upon successful creation this should return a "success" message,
#   and the resulting Budget object data
@router.put("/budget/create", response_model=schemas.Budget)
def create_budget(db: Session = Depends(get_db)):
    return budget_create(db)

###
# Partial update for the Budget model
# - Return if update is successful
@router.patch("/budget/update", response_model=schemas.PartialBudget)
def update_budget(partial_budget: PartialBudget, db:Session = Depends(get_db)):
    return budget_update(partial_budget, db)

###
# Delete a budget record from the database
@router.delete("/budget/delete/{id}")
def delete_budget(id, db: Session = Depends(get_db)):
    return budget_delete(id, db)