from fastapi import APIRouter, HTTPException, status, Depends
from tortoise.exceptions import DoesNotExist
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from schemas.user import UserCreate, UserLogin, UserOut
from models.user import User
load_dotenv()
router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

async def get_user_by_email(email: str):
    try:
        return await User.get(email=email)
    except DoesNotExist:
        return None

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/signup", response_model=UserOut)
async def signup(user: UserCreate):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    user_obj = await User.create(
        firstName=user.firstName,
        lastName=user.lastName,
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    return UserOut(id=user_obj.id, username=user_obj.username, email=user_obj.email)

@router.post("/login")
async def login(user: UserLogin):
    db_user = await get_user_by_email(user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": db_user.username})
    return {
        "status": "success",
        "user": {   # 👈 fixed here (added quotes)
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email
        },
        "access_token": access_token,
    }