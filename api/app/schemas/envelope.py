import decimal
from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime
from datetime import date


class Envelope(BaseModel):
    id: uuid.UUID
    date_created: datetime
    name: str
    spent: decimal.Decimal
    budget: decimal.Decimal
    category_id: uuid.UUID

class PartialEnvelope(BaseModel):
    id: uuid.UUID
    date_created: Optional[datetime] = None
    name: Optional[str] = None
    spent: Optional[decimal.Decimal] = None
    budget: Optional[decimal.Decimal] = None
    category_id: Optional[uuid.UUID] = None