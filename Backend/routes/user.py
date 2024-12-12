from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.user import User
from config.database import get_db
from schemas.user import RegisterRequest, RegisterResponse, LoginRequest, forgetpasswordRequest, ResetPasswordRequest
from middlewares.jwt_auth import hash_password, create_access_token, verify_password, create_reset_password_token
from middlewares.mail_send import send_email
from uuid import UUID
import jwt
import os



SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"

router = APIRouter()

# User registration
@router.post("/register", response_model=RegisterResponse)
def register_user(user: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already registered.")

    new_user = User(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return RegisterResponse(message="User registered successfully.", user_id=new_user.id)


# User login (returns JWT token)
@router.post("/login")
def login_user(user: LoginRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user or not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials.")

    # Convert UUID to string for the JWT payload
    access_token = create_access_token(data={"sub": str(existing_user.id), "email": existing_user.email})
    return {"access_token": access_token, "id": existing_user.id }


@router.post("/forget-password")
def forget_password(user: forgetpasswordRequest, db: Session = Depends(get_db)):
    """Handle forget password requests."""
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found.")

    reset_token = create_reset_password_token(existing_user.email)
    reset_link = f"http://127.0.0.1:8000/reset-password?token={reset_token}"
    email_body = f"""
    Hi {existing_user.firstname+" "+existing_user.lastname},

    You requested to reset your password. Use the link below to reset it:
    {reset_link}

    This link will expire in 10 minutes.

    If you did not request this, please ignore this email.

    Regards,
    Grocery Team
    """
    # send_email(existing_user.email, "Password Reset Request", email_body)
    
    mail = (existing_user.email, "Password Reset Request", email_body)
    
    
    return {"message": "Password reset instructions sent to your email." , "gmail:": mail}


@router.post("/reset-password")
def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    """Endpoint to reset the user's password."""
    try:
        # Decode the token
        payload = jwt.decode(request.token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=403, detail="Invalid token.")
        
        # Fetch the user from the database
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found.")
        
        # Hash the new password
        hashed_password = hash_password(request.new_password)
        
        # Update the password in the database
        user.password = hashed_password
        db.commit()

        return {"message": "Password has been updated successfully."}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token has expired.")
    except jwt.PyJWTError:
        raise HTTPException(status_code=403, detail="Invalid token.")