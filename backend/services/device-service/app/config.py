import os
from dotenv import load_dotenv

load_dotenv()  # loads root .env

class Config:
    # Core Flask
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("FLASK_ENV") == "development"

    # Communication
    API_SERVICE_URL = os.getenv("API_SERVICE_URL")

    # Device-specific
    DEVICE_TIMEOUT = int(os.getenv("DEVICE_TIMEOUT", 5))
    MAX_PAYLOAD_SIZE = int(os.getenv("MAX_PAYLOAD_SIZE", 1024))
