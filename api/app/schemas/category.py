from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime
from datetime import date


class Category(BaseModel):
    id: uuid.UUID
    date_created: datetime
    name: str
    budget_id: uuid.UUID

class PartialCategory(BaseModel):
    id: uuid.UUID
    date_created: Optional[datetime] = None
    name: Optional[str] = None
    budget_id: Optional[uuid.UUID] = None