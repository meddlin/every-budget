import uuid
from sqlalchemy import Column, ForeignKey, Table, column
from sqlalchemy.sql import func
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import engine, metadata, Base

""" class Budget(Base):
    __table__ = Table(
        "budget", 
        metadata, 
        sqlalchemy.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sqlalchemy.Column("date_created", sqlalchemy.DateTime),
        sqlalchemy.Column("name", sqlalchemy.String)
    ) """

class Budget(Base):
    __tablename__ = "budget"

    id = Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    date_created = Column(sqlalchemy.DateTime, server_default = func.now())
    # updated_at = Column(sqlalchemy.DateTime, onupdate = func.now())
    name = Column(sqlalchemy.String)

    categories = relationship("Category", back_populates = "budget")

    ### """
    # It's best practice to set the value of __repr__ on data models 
    # (and Python classes in general) for the purpose of logging or 
    # debugging our class instances. The value returned by __repr__ 
    # is what we'll see when we print() an instance of User. If you've 
    # ever had to deal with [object Object] in Javascript, you're 
    # already familiar with how obnoxious it is to debug an object's 
    # value and receive nothing useful in return.
    # """

    def __repr__(self):
        return f"<Budget {self.name}>"

""" class Category(Base):
    __table__ = Table(
        "category",
        metadata, 
        sqlalchemy.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sqlalchemy.Column("date_created", sqlalchemy.DateTime),
        sqlalchemy.Column("name", sqlalchemy.String),
        sqlalchemy.Column("budget_id", UUID(as_uuid=True))
    ) """
class Category(Base):
    __tablename__ = "category"

    id = Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    date_created = Column(sqlalchemy.DateTime, server_default = func.now())
    # updated_at = Column(sqlalchemy.DateTime, onupdate = func.now())
    name = Column(sqlalchemy.String)
    budget_id = Column(UUID(as_uuid = True), ForeignKey("budget.id"))

    # Relationship
    budget = relationship("Budget", back_populates = "categories")

    def __repr__(self):
        return f"<Category {self.id}>"

""" class Envelope(Base):
    __table__ = Table(
        "envelope",
        metadata, 
        sqlalchemy.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sqlalchemy.Column("date_created", sqlalchemy.DateTime),
        sqlalchemy.Column("name", sqlalchemy.String),
        sqlalchemy.Column("spent", sqlalchemy.Numeric),
        sqlalchemy.Column("budget", sqlalchemy.Numeric),
        sqlalchemy.Column("category_id", UUID(as_uuid=True))
    ) """

class Envelope(Base):
    __tablename__ = "envelope"

    id = Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    date_created = Column(sqlalchemy.DateTime, server_default = func.now())
    # updated_at = Column(sqlalchemy.DateTime, onupdate = func.now())
    name = Column(sqlalchemy.String)
    spent = Column(sqlalchemy.Numeric)
    budget = Column(sqlalchemy.Numeric)
    category_id = Column(UUID(as_uuid = True), ForeignKey("category.id"))

    # Relationship
    category = relationship("Category")

    def __repr__(self):
        return f"<Envelope {self.id}>"

""" class Transaction(Base):
    __table__ = Table(
        "transaction",
        metadata, 
        sqlalchemy.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sqlalchemy.Column("date_created", sqlalchemy.DateTime),
        sqlalchemy.Column("date_added", sqlalchemy.DateTime),
        sqlalchemy.Column("vendor", sqlalchemy.String),
        sqlalchemy.Column("amount", sqlalchemy.Numeric),
        sqlalchemy.Column("note", sqlalchemy.String),
        sqlalchemy.Column("envelope_id", UUID(as_uuid=True))
    ) """

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    date_created = Column(sqlalchemy.DateTime, server_default = func.now())
    date_added = Column(sqlalchemy.DateTime, server_default = func.now())
    # updated_at = Column(sqlalchemy.DateTime, onupdate = func.now())
    vendor = Column(sqlalchemy.String)
    amount = Column(sqlalchemy.Numeric)
    note = Column(sqlalchemy.String)
    envelope_id = Column(UUID(as_uuid = True), ForeignKey("envelope.id"))

    # Relationship
    envelope = relationship("Envelope")

    def __repr__(self):
        return f"<Transaction {self.id}>"