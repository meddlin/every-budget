from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter

from app.schemas import schemas
from app.routers.helpers import envelope_single
from app.database.database import get_db

from datetime import date

router = APIRouter()

@router.get("/envelope/{id}", response_model=schemas.Envelope)
def get_envelope(id, db: Session = Depends(get_db)):
    return envelope_single(id, db)