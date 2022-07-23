import datetime
import uuid
from sqlalchemy import func, select, insert
import sqlalchemy
from sqlalchemy.orm import Session
from app.schemas.transaction import PartialTransaction
from app.database.models import Transaction

from datetime import date


def transaction_single(id: uuid, db: Session):
    ## pseudo-SQL: select 1 budget where id == {id}
    transaction = db.query().filter(Transaction.id == id)
    if not transaction:
        return False
    return transaction

###
# Select all Budget records in the database
# - TODO: This is a "select *" query for prototyping. Limit this query later!
def transactions_get_all(db: Session):
    transactions = db.query(Transaction.id, Transaction.date_created, Transaction.vendor).all()

    if not transactions:
        return False
    return transactions

def transaction_create(db: Session):
    transaction = Transaction(
        id = uuid.uuid4(), 
        date_created = datetime.datetime.now(),
        vendor = "",
        amount = 0.00,
        note = "this is a test transaction",
        envelope_id = uuid.uuid4()
    )
    db.add(transaction)
    db.commit()

def transaction_update(partial_transaction: PartialTransaction, db: Session):
    # budget = Budget() # update here
    res = db.query(Transaction).filter(Transaction.id == Transaction.id).update(
        {
            Transaction.vendor: partial_transaction.vendor
        }, 
        synchronize_session = False
    )
    print("Result from transaction_update")
    print(res)
    db.commit()

###
# Remove an Envelope record
def transaction_delete(id, db: Session):
    res = db.query(Transaction).filter(Transaction.id == id).delete()
    print("Result from transaction_delete")
    print(res)
    db.commit()