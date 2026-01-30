from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.ai.chatbot import chat_with_ai
from app.database import get_db
from app.crud.ticket import create_ticket
from app.schemas.ticket import TicketCreate

router = APIRouter(prefix="/chat", tags=["AI Chat"])

class ChatRequest(BaseModel):
    message: str
    guest_id: int

@router.post("/")
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    ai_result = chat_with_ai(req.message)

    # If AI decides to raise a ticket
    if ai_result.get("intent") == "raise_ticket":
        ticket_data = TicketCreate(
            guest_id=req.guest_id,
            issue_type=ai_result["issue_type"],
            description=ai_result["description"]
        )

        ticket = create_ticket(db, ticket_data)

        return {
            "reply": "Your issue has been reported successfully.",
            "ticket_id": ticket.id,
            "department_id": ticket.department_id
        }

    # Otherwise normal chat response
    return {
        "reply": ai_result.get("message", "How can I help you?")
    }
