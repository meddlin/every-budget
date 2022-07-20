import datetime
import uuid
from sqlalchemy import func, select, insert
import sqlalchemy
from sqlalchemy.orm import Session

from app.database.models import Transaction

from datetime import date


def transaction_single(id: uuid, db: Session):
    ## pseudo-SQL: select 1 budget where id == {id}
    transaction = db.query().filter(Transaction.id == id)
    if not transaction:
        return False
    return transaction