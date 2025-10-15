from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    firstName: str
    lastName: str
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr