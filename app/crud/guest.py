from sqlalchemy.orm import Session
from app.models.guest import Guest
from app.schemas.guest import GuestCreate

def create_guest(db: Session, guest: GuestCreate):
    db_guest = Guest(
        name=guest.name,
        email=guest.email,
        phone=guest.phone
    )
    db.add(db_guest)
    db.commit()
    db.refresh(db_guest)
    return db_guest

def get_all_guests(db: Session):
    return db.query(Guest).all()
