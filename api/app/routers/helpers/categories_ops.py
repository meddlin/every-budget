import datetime
import uuid
from sqlalchemy import func, select, insert
import sqlalchemy
from sqlalchemy.orm import Session
from datetime import date

from app.database.models import Category

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
    print('reached category_insert_single')

    cat = Category(
        id = uuid.uuid4(), 
        date_created = datetime.datetime.now(), 
        name = sample_cat.name, 
        budget_id = sample_cat.budget_id
    )
    # hardcode_category = Category(date_created = datetime.datetime.now(), name = 'Jan')
    db.add(cat)

    # query = Category.insert().values( id = uuid.uuid4(), date_created = datetime.datetime.now(), name = 'Jan' )
    # db.execute(query)
    db.commit()