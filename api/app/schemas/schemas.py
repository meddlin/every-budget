from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime
from datetime import date


class Envelope(BaseModel):
    id: uuid.UUID
    date_created: datetime
    name: str


class Transaction(BaseModel):
    id: uuid.UUID