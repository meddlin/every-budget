from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime
from datetime import date

class Budget(BaseModel):
    id: uuid.UUID
    date_created: datetime
    name: str

class PartialBudget(BaseModel):
    id: uuid.UUID
    date_created: Optional[datetime] = None
    name: Optional[str] = None



class Category(BaseModel):
    id: uuid.UUID
    date_created: datetime
    name: str
    budget_id: uuid.UUID


class Envelope(BaseModel):
    id: uuid.UUID
    date_created: datetime
    name: str


class Transaction(BaseModel):
    id: uuid.UUID