import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from passlib.context import CryptContext
from config.database import get_db
from sqlalchemy.orm import Session
from models.user import User
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from dotenv import load_dotenv


import os

# Load environment variables
load_dotenv()

# Secret key for JWT signing (ensure you set this in your .env file)
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2PasswordBearer instance for getting token from the request header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# CryptContext instance for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired.")
    except jwt.JWTError:
        raise HTTPException(status_code=403, detail="Invalid token.")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    payload = verify_token(token)
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=403, detail="Invalid token.")
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return user

# Create a token for the user to reset password
def create_reset_password_token(email: str) -> str:
    """Generate a reset password token for a given email."""
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(minutes=10)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# varify the reset password token
def verify_reset_password_token(token: str, db: Session = Depends(get_db)):
    payload = verify_token(token)
    email = payload.get("email")
    if email is None:
        raise HTTPException(status_code=403, detail="Invalid token.")
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return token




