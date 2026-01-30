import os
from dotenv import load_dotenv

load_dotenv()  

DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL")
