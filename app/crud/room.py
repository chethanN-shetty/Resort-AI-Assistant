from sqlalchemy.orm import Session
from app.models.room import Room
from app.schemas.room import RoomCreate

def create_room(db: Session, room: RoomCreate):
    db_room = Room(
        room_number=room.room_number,
        room_type=room.room_type,
        price_per_night=room.price_per_night
    )
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def get_all_rooms(db: Session):
    return db.query(Room).all()
