import decimal
from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime
from datetime import date

###
# Pydantic models for Transaction-related objects
###

###
# Transaction: main class for most operations surrounding Transaction
class Transaction(BaseModel):
    id: uuid.UUID
    date_created: datetime
    date_added: datetime
    vendor: str
    amount: decimal.Decimal
    note: str
    envelope_id: uuid.UUID

class PartialTransaction(BaseModel):
    id: uuid.UUID
    date_created: Optional[datetime] = None
    date_added: Optional[datetime] = None
    vendor: Optional[str] = None
    amount: Optional[decimal.Decimal] = None
    note: Optional[str] = None
    envelope_id: Optional[uuid.UUID] = None