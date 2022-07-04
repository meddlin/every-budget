import uuid
from sqlalchemy import Column, Table, column
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import engine, metadata, Base

class Budget(Base):
    __table__ = Table(
        "budget", 
        metadata, 
        sqlalchemy.Column("id", UUID, primary_key=True, default=uuid.uuid4),
        sqlalchemy.Column("date_created", sqlalchemy.DateTime),
        sqlalchemy.Column("name", sqlalchemy.String)
    )

# class Category(Base):
#     __table__ = Table(
#         "category",
#         metadata, 
#         sqlalchemy.Column("id", UUID, primary_key=True, default=uuid.uuid4),
#         sqlalchemy.Column("date_created", sqlalchemy.DateTime),
#         sqlalchemy.Column("name", sqlalchemy.String),
#         sqlalchemy.Column("budget_id", UUID)
#     )

# class Envelope(Base):
#     __table__ = Table(
#         "envelope",
#         metadata, 
#         sqlalchemy.Column("id", UUID, primary_key=True, default=uuid.uuid4),
#         sqlalchemy.Column("date_created", sqlalchemy.DateTime),
#         sqlalchemy.Column("name", sqlalchemy.String),
#         sqlalchemy.Column("spent", sqlalchemy.Numeric),
#         sqlalchemy.Column("budget", sqlalchemy.Numeric),
#         sqlalchemy.Column("category_id", UUID)
#     )

# class Transaction(Base):
#     __table__ = Table(
#         "transaction",
#         metadata, 
#         sqlalchemy.Column("id", UUID, primary_key=True, default=uuid.uuid4),
#         sqlalchemy.Column("date_created", sqlalchemy.DateTime),
#         sqlalchemy.Column("date_added", sqlalchemy.DateTime),
#         sqlalchemy.Column("vendor", sqlalchemy.String),
#         sqlalchemy.Column("amount", sqlalchemy.Numeric),
#         sqlalchemy.Column("note", sqlalchemy.String),
#         sqlalchemy.Column("envelope_id", UUID)
#     )