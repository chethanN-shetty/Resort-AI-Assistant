from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    guest_id = Column(Integer, ForeignKey("guests.id"))
    department_id = Column(Integer, ForeignKey("departments.id"))
    issue_type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, default="open")
