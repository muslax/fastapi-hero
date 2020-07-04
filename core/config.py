import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME        = os.getenv("PROJECT_NAME", "FastAPI Config")

MONGODB_URI          = os.getenv("MONGODB_URI")
MONGODB_NAME         = os.getenv("MONGODB_NAME")
MONGODB_MAX_POOL_SIZE=100
MONGODB_MIN_POOL_SIZE=10

SENTRY_DSN           = os.getenv("SENTRY_DSN")

SMTP_HOST            = os.getenv("SMTP_HOST")
SMTP_USER            = os.getenv("SMTP_USER")
SMTP_PASSWORD        = os.getenv("SMTP_PASSWORD")
EMAILS_FROM_EMAIL    = os.getenv("EMAILS_FROM_EMAIL")

