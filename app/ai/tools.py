import requests
import os

BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL")


def raise_ticket_tool(guest_id: int, issue_type: str, description: str):
    payload = {
        "guest_id": guest_id,
        "issue_type": issue_type,
        "description": description
    }

    response = requests.post(
        f"{BACKEND_BASE_URL}/tickets/",
        json=payload,
        timeout=10
    )

    response.raise_for_status()
    return response.json()
