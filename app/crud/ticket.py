from sqlalchemy.orm import Session
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate
from app.models.department import Department


def get_department_id(db: Session, issue_type: str):
    mapping = {
        "cleaning": "Housekeeping",
        "maintenance": "Maintenance",
        "lost_item": "Security",
        "billing": "Front Desk"
    }

    department_name = mapping.get(issue_type.lower())
    if not department_name:
        return None

    department = (
        db.query(Department)
        .filter(Department.name == department_name)
        .first()
    )

    return department.id if department else None


def create_ticket(db: Session, ticket: TicketCreate):
    department_id = get_department_id(db, ticket.issue_type)

    db_ticket = Ticket(
        guest_id=ticket.guest_id,
        issue_type=ticket.issue_type,
        description=ticket.description,
        department_id=department_id,
        status="open"
    )

    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def get_all_tickets(db: Session):
    return db.query(Ticket).all()
