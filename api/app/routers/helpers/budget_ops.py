import datetime
import uuid
from sqlalchemy import func, select, insert
import sqlalchemy
from sqlalchemy.orm import Session, Load, joinedload
from datetime import date
from app.database.models import Transaction
from app.database.models import Envelope
from app.database.models import Category
from app.database.models import Budget

from app.schemas.budget import BudgetDetail as PydanticBudget
from app.schemas.category import PartialCategory as PydanticCategory

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

    if not budget:
        return False
    return budget

def budget_full_detail(id, db: Session):
    print('in budget_ops.py - budget_full_detail')
    """select
    * 
    from budget
    join category
        on budget.id = category.budget_id
    join envelope
        on category.id = envelope.category_id
    join transaction
        on envelope.id = transaction.envelope_id
    """

    """ res = db.query(
            Budget.id.label('budget_id'),
            Budget.date_created.label('budget_date_created'),
            Budget.name.label('budget_name'),
            Category.id.label('category_id'),
            Category.date_created.label('category_date_created'),
            Category.name.label('category_name'),
            Category.budget_id.label('category_budget_id')
        ).join(Category).filter(Budget.id == Category.budget_id).first() """
    
    res = db.query(
            Budget.id.label('budget_id'),
            Budget.date_created.label('budget_date_created'),
            Budget.name.label('budget_name'),
            Category.id.label('category_id'),
            Category.date_created.label('category_date_created'),
            Category.name.label('category_name'),
            Category.budget_id.label('category_budget_id'),
            Envelope.id.label('envelope_id'),
            Transaction.id.label('transaction_id')
        ).join(Category, Budget.id == Category.budget_id
        ).join(Envelope, Category.id == Envelope.category_id
        ).join(Transaction, Envelope.id == Transaction.envelope_id).all()
    
    for r in res:
        print(r)
    
    print('PRINTING res...')
    print(res)
    print('PRINTING KEYS...')
    print(res.keys())

    keys = []
    for key in res.keys():
        keys.append(key)

    mydata = {}
    """ for key in res.keys():
        # print(key)
        mydata[key] = "" """

    i = 0
    while i < len(keys):
        mydata[keys[i]] = res[i]
        i += 1

    budget = PydanticBudget(
        id = mydata['budget_id'],
        date_created = mydata['budget_date_created'],
        name = mydata['budget_name'],
        category = PydanticCategory(
            id = mydata['category_id'],
            date_created = mydata['category_date_created'],
            name = mydata['category_name'],
            budget_id = mydata['category_budget_id']
        )
    )
    
    print(budget)
    # print(category)

    return res

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