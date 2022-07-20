import datetime
import uuid
from sqlalchemy import func, select, insert
import sqlalchemy
from sqlalchemy.orm import Session
from datetime import date
from app.schemas.category import PartialCategory

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

def categories_get_all(db: Session):
    categories = db.query(
        Category.id, 
        Category.date_created,
        Category.name,
        Category.budget_id
    ).all()

    if not categories:
        return False
    return categories

###
# Insert a single Category record
def category_insert_single(db: Session):
    print('reached category_insert_single')

    cat = Category(
        id = uuid.uuid4(), 
        date_created = datetime.datetime.now(), 
        name = "example", 
        budget_id = uuid.uuid4()
    )

    db.add(cat)
    db.commit()

###
# Update non-key, non-metrics fields on Category records
def category_update(partial_category: PartialCategory, db: Session):
    print("...")
    print("IN CATEGORY_UPDATE")
    print(partial_category)

    # budget = Budget() # update here
    res = db.query(Category).filter(Category.id == partial_category.id).update(
        {
            Category.name: partial_category.name
        }, 
        synchronize_session = False
    )
    print("Result from category_update")
    print(res)
    db.commit()

###
# Remove a Category record
def category_delete(id, db: Session):
    res = db.query(Category).filter(Category.id == id).delete()
    print("Result from category_delete")
    print(res)
    db.commit()