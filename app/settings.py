"""Settings for the app."""

import os
from pathlib import Path

from dotenv import load_dotenv

from app.adapter.app_exception import AppException

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise AppException("No OPENAI_API_KEY set for OpenAI API")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise AppException("No GROQ_API_KEY set for Groq API")


RECORDING_DIR = Path(__file__).parent / "core" / "records"
