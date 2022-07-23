from typing import List
from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter

from app.schemas.envelope import Envelope, PartialEnvelope
from app.routers.helpers.envelopes_ops import envelope_single, envelopes_get_all, envelope_create, envelope_update, envelope_delete
from app.database.database import get_db

from datetime import date

router = APIRouter()

@router.get("/envelope/{id}", response_model=Envelope)
def get_envelope(id, db: Session = Depends(get_db)):
    return envelope_single(id, db)

@router.post("/envelope/get_all", response_model = List[Envelope])
def get_all_envelopes(db: Session = Depends(get_db)):
    return envelopes_get_all(db)

@router.put("/envelope/create", response_model=Envelope)
def create_envelope(db: Session = Depends(get_db)):
    return envelope_create(db)

@router.patch("/envelope/patch", response_model=PartialEnvelope)
def update_envelope(partial: PartialEnvelope, db: Session = Depends(get_db)):
    return envelope_update(partial, db)

@router.delete("/envelope/delete/{id}")
def delete_envelope(id, db: Session = Depends(get_db)):
    return envelope_delete(id, db)