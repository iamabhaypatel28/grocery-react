from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    firstname:str
    lastname: str
    email: EmailStr
    password: str

class RegisterResponse(BaseModel):
    message: str
    user_id: int
