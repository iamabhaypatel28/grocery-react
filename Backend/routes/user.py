from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.user import User
from config.database import get_db
from schemas.user import RegisterRequest, RegisterResponse, LoginRequest
from middlewares.jwt_auth import hash_password, create_access_token, verify_password
from uuid import UUID
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


@router.get("/status")
def get_status():
    return {"status": "success"}
