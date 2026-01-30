from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.guest import GuestCreate, GuestResponse
from app.crud.guest import create_guest, get_all_guests

router = APIRouter(prefix="/guests", tags=["Guests"])

@router.post("/", response_model=GuestResponse)
def add_guest(guest: GuestCreate, db: Session = Depends(get_db)):
    return create_guest(db, guest)

@router.get("/", response_model=list[GuestResponse])
def list_guests(db: Session = Depends(get_db)):
    return get_all_guests(db)
