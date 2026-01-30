from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.guest import router as guest_router
from app.api.room import router as room_router
from app.api.booking import router as booking_router
from app.api.ticket import router as ticket_router
from app.api.chat import router as chat_router

app = FastAPI(title="Resort AI Assistant")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(guest_router)
app.include_router(room_router)
app.include_router(booking_router)
app.include_router(ticket_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "Resort AI is running"}
