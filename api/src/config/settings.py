from pathlib import Path
from decouple import config

SECRET_KEY = config("SECRET_KEY")

BASE_DIR = Path(__file__).resolve().parent.parent

# MONGO DB CREDS(MONGODB)

MONGO_HOST = config("MONGO_HOST", default="mongo")
MONGO_PORT = config("MONGO_PORT", default=27017, cast=int)
MONGO_DB = config("MONGO_DB")

#RELATIONAL DB CREDS(POSTGRESQL)

DB_USER = config("postgres")
DB_PASSWORD = config("lkm13464")
DB_HOST = config("localhost")
DB_NAME = config("trapper_db")
DB_PORT = config("5432")



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:4200",
    "http://localhost:8080",
    ]



# Application definition

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

SERVICE_ROUTES = {
    "auth_service": "http://127.0.0.1:8001/auth/api",
    "booking_service": "http://localhost:8005",
    "email_service": "http://localhost:8000",
    "rent_services": "http://localhost:8000",
    "wallet_service": "https://localhost:8010"
}


