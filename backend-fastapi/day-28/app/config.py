from dotenv import load_dotenv
import os

# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

APP_NAME = os.getenv(
    "APP_NAME"
)