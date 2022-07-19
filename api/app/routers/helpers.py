import datetime
import uuid
from sqlalchemy import func, select, insert
import sqlalchemy
from sqlalchemy.orm import Session

from app.database.models import Budget
from app.database.models import Category
from app.database.models import Envelope
from app.database.models import Transaction

from datetime import date

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


def budget_delete(id, db: Session):
    #budget = Budget() # delete query here
    res = db.query(Budget).filter(Budget.id == id).delete()
    print("Result from budget_delete")
    print(res)
    db.commit()


def category_single(id: uuid, db: Session):
    ## pseudo-SQL: select 1 budget where id == {id}
    category = db.query(
        Category.id,
        Category.date_created,
        Category.name,
        Category.budget_id
    ).filter(
        Category.id == id
    ).first()
    if not category:
        return False
    return category

def category_insert_single(sample_cat, db: Session):
    # print('passed in..')
    # print(category)

    print('reached category_insert_single')

    cat = Category(id = uuid.uuid4(), date_created = datetime.datetime.now(), name = sample_cat.name, budget_id = sample_cat.budget_id)
    # hardcode_category = Category(date_created = datetime.datetime.now(), name = 'Jan')
    db.add(cat)

    # query = Category.insert().values( id = uuid.uuid4(), date_created = datetime.datetime.now(), name = 'Jan' )
    # db.execute(query)
    db.commit()


def envelope_single(id: uuid, db: Session):
    ## pseudo-SQL: select 1 budget where id == {id}
    envelope = db.query().filter(Envelope.id == id)
    if not envelope:
        return False
    return envelope

def transaction_single(id: uuid, db: Session):
    ## pseudo-SQL: select 1 budget where id == {id}
    transaction = db.query().filter(Transaction.id == id)
    if not transaction:
        return False
    return transaction