import datetime
import uuid
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.database.models import Budget
# from app.database.models import Category
# from app.database.models import Envelope
# from app.database.models import Transaction

from datetime import date

def budget_single(id: uuid, db: Session):
    ## pseudo-SQL: select 1 budget where id == {id}
    # budget = db.query().filter(Budget.id == id)
    budget = db.query(
        Budget.id,
        Budget.date_created,
        Budget.name
    ).first()

    # budget = { 
    #     'id': uuid.uuid4(),
    #     'date_created': datetime.datetime.now(),
    #     'name': "test return" 
    # }

    if not budget:
        return False
    return budget

# def category_single(id: id, db: Session):
#     ## pseudo-SQL: select 1 budget where id == {id}
#     category = db.query().filter(Category.id == id)
#     if not category:
#         return False
#     return category

# def envelope_single(id: id, db: Session):
#     ## pseudo-SQL: select 1 budget where id == {id}
#     envelope = db.query().filter(Envelope.id == id)
#     if not envelope:
#         return False
#     return envelope

# def transaction_single(id: id, db: Session):
#     ## pseudo-SQL: select 1 budget where id == {id}
#     transaction = db.query().filter(Transaction.id == id)
#     if not transaction:
#         return False
#     return transaction