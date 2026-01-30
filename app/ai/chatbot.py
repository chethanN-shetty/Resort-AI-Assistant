import json
from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.ai.prompts import SYSTEM_PROMPT
from app.ai.tools import raise_ticket_tool

client = OpenAI(api_key=OPENAI_API_KEY)



def chat_with_ai(user_message: str):
    msg = user_message.lower()

    # Simple intent detection (AI logic simulation)
    if "ac" in msg or "not working" in msg or "maintenance" in msg:
        return {
            "intent": "raise_ticket",
            "issue_type": "maintenance",
            "description": user_message
        }

    if "clean" in msg or "housekeeping" in msg:
        return {
            "intent": "raise_ticket",
            "issue_type": "cleaning",
            "description": user_message
        }

    if "lost" in msg:
        return {
            "intent": "raise_ticket",
            "issue_type": "lost_item",
            "description": user_message
        }

    if "book" in msg or "reservation" in msg:
        return {
            "intent": "booking_query",
            "message": "I can help you with room bookings."
        }

    return {
        "intent": "general_query",
        "message": "How can I help you today?"
    }
