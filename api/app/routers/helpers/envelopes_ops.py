import datetime
import uuid
from sqlalchemy import func, select, insert
import sqlalchemy
from sqlalchemy.orm import Session
from app.database.models import Envelope

from datetime import date

def envelope_single(id: uuid, db: Session):
    ## pseudo-SQL: select 1 budget where id == {id}
    envelope = db.query().filter(Envelope.id == id)
    if not envelope:
        return False
    return envelope