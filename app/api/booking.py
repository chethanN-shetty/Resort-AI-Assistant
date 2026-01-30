from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.booking import BookingCreate, BookingResponse
from app.crud.booking import create_booking, get_all_bookings

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/", response_model=BookingResponse)
def add_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    db_booking = create_booking(db, booking)
    if not db_booking:
        raise HTTPException(
            status_code=400,
            detail="Room is already booked for selected dates"
        )
    return db_booking

@router.get("/", response_model=list[BookingResponse])
def list_bookings(db: Session = Depends(get_db)):
    return get_all_bookings(db)
