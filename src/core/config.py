import os

from dotenv import load_dotenv

load_dotenv()

# Database
DATABASE_URL = os.getenv("DATABASE_URL")

# JWT
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "hello_world")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

# OTP
OTP_CODE_EXPIRE_MINUTES = int(os.getenv("OTP_CODE_EXPIRE_MINUTES", "10"))
