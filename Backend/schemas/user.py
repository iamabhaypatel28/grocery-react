from pydantic import BaseModel, EmailStr
from uuid import UUID

class RegisterRequest(BaseModel):
    firstname:str
    lastname: str
    email: EmailStr
    password: str

class RegisterResponse(BaseModel):
    message: str
    user_id: UUID


class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    
class forgetpasswordRequest(BaseModel):
    email : EmailStr
    
class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str