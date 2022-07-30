from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime
from datetime import date
from app.schemas.category import Category, PartialCategory

class Budget(BaseModel):
    id: uuid.UUID
    date_created: datetime
    name: str

    class Config:
        orm_mode = True

class BudgetDetail(BaseModel):
    id: uuid.UUID
    date_created: Optional[datetime] = None
    name: str
    category: PartialCategory

    class Config:
        orm_mode = True

class PartialBudget(BaseModel):
    id: uuid.UUID
    date_created: Optional[datetime] = None
    name: Optional[str] = None