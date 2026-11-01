import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing")

if not OPEN_ROUTER_API_KEY:
    raise ValueError("OPEN_ROUTER_API_KEY is missing")

if not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY is missing")