import datetime
import uuid
from sqlalchemy import func, select, insert
import sqlalchemy
from sqlalchemy.orm import Session
from datetime import date

from app.database.models import Budget

###
# Retrieve a single Budget record from the database.
def budget_single(id: uuid, db: Session):
    ## pseudo-SQL: select 1 budget where id == {id}
    
    budget = db.query(
        Budget.id,
        Budget.date_created,
        Budget.name
    ).filter(
        Budget.id == id
    ).first()

    # budget = { 
    #     'id': uuid.uuid4(),
    #     'date_created': datetime.datetime.now(),
    #     'name': "test return" 
    # }

    if not budget:
        return False
    return budget

###
# Select all Budget records in the database
# - TODO: This is a "select *" query for prototyping. Limit this query later!
def budget_get_all(db: Session):
    budgets = db.query(Budget.id, Budget.date_created, Budget.name).all()
    print("in budget_get_all...")
    print(budgets)

    if not budgets:
        return False
    return budgets

###
# Insert a Budget record
def budget_create(db: Session):
    budget = Budget(
        id = uuid.uuid4(), 
        date_created = datetime.datetime.now(),
        name = "")
    db.add(budget)
    db.commit()
    
    # Use `.refresh()` to pull a "result" after the INSERT sql statement
    # Ref: https://stackoverflow.com/questions/19388555/sqlalchemy-session-add-return-value
    db.refresh(budget)
    print("... watch for refresh")
    print(budget)
    print(budget.id)

###
# Update non-key, non-metrics fields on Budget records
def budget_update(partial_budget, db: Session):
    print("...")
    print("IN BUDGET_UPDATE")
    print(partial_budget)

    # budget = Budget() # update here
    res = db.query(Budget).filter(Budget.id == partial_budget.id).update(
        {
            Budget.name: partial_budget.name
        }, 
        synchronize_session = False
    )
    print("Result from budget_update")
    print(res)
    db.commit()

###
# Remove a Budget record
def budget_delete(id, db: Session):
    #budget = Budget() # delete query here
    res = db.query(Budget).filter(Budget.id == id).delete()
    print("Result from budget_delete")
    print(res)
    db.commit()