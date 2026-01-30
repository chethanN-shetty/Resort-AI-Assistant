from app.database import engine, Base
from app.models.guest import Guest
from app.models.room import Room
from app.models.booking import Booking
from app.models.ticket import Ticket
from app.models.department import Department


print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
