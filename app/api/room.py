from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.room import RoomCreate, RoomResponse
from app.crud.room import create_room, get_all_rooms

router = APIRouter(prefix="/rooms", tags=["Rooms"])

@router.post("/", response_model=RoomResponse)
def add_room(room: RoomCreate, db: Session = Depends(get_db)):
    return create_room(db, room)

@router.get("/", response_model=list[RoomResponse])
def list_rooms(db: Session = Depends(get_db)):
    return get_all_rooms(db)
