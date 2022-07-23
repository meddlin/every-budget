import datetime
import uuid
from sqlalchemy import func, select, insert
import sqlalchemy
from sqlalchemy.orm import Session
from app.schemas.envelope import PartialEnvelope
from app.database.models import Envelope
from datetime import date


def envelope_single(id: uuid, db: Session):
    ## pseudo-SQL: select 1 budget where id == {id}
    envelope = db.query().filter(Envelope.id == id).first()

    if not envelope:
        return False
    return envelope

###
# Select all Budget records in the database
# - TODO: This is a "select *" query for prototyping. Limit this query later!
def envelopes_get_all(db: Session):
    envelopes = db.query(Envelope.id, Envelope.date_created, Envelope.name).all()

    if not envelopes:
        return False
    return envelopes

def envelope_create(db: Session):
    envelope = Envelope(
        id = uuid.uuid4(), 
        date_created = datetime.datetime.now(),
        name = "",
        spent = 0.00,
        budget = 0.00,
        category_id = uuid.uuid4()
    )
    db.add(envelope)
    db.commit()
    
    # Use `.refresh()` to pull a "result" after the INSERT sql statement
    # Ref: https://stackoverflow.com/questions/19388555/sqlalchemy-session-add-return-value
    db.refresh(envelope)
    print("... watch for refresh")
    print(envelope)
    print(envelope.id)

def envelope_update(partial_envelope: PartialEnvelope, db: Session):
    # budget = Budget() # update here
    res = db.query(Envelope).filter(Envelope.id == partial_envelope.id).update(
        {
            Envelope.name: partial_envelope.name
        }, 
        synchronize_session = False
    )
    print("Result from envelope_update")
    print(res)
    db.commit()

###
# Remove an Envelope record
def envelope_delete(id, db: Session):
    res = db.query(Envelope).filter(Envelope.id == id).delete()
    print("Result from envelope_delete")
    print(res)
    db.commit()