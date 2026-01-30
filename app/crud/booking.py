from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.booking import Booking
from app.schemas.booking import BookingCreate

def is_room_available(db: Session, room_id: int, check_in, check_out):
    overlapping_booking = db.query(Booking).filter(
        Booking.room_id == room_id,
        Booking.check_out > check_in,
        Booking.check_in < check_out
    ).first()
    return overlapping_booking is None

def create_booking(db: Session, booking: BookingCreate):
    if not is_room_available(db, booking.room_id, booking.check_in, booking.check_out):
        return None

    db_booking = Booking(
        guest_id=booking.guest_id,
        room_id=booking.room_id,
        check_in=booking.check_in,
        check_out=booking.check_out
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
    
def get_all_bookings(db: Session):
    return db.query(Booking).all()
