# auth_routes.py
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import SessionLocal
from schema import SignUpModel, LoginModel
from models import User
from werkzeug.security import generate_password_hash
from fastapi_jwt_auth import AuthJWT

auth_router = APIRouter(prefix="/auth", tags=["auth"])


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@auth_router.get("/")
async def hello():
    return {"message": "Hello World"}


@auth_router.post("/signup", response_model=SignUpModel, status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel, db: Session = Depends(get_db)):
    db_email = db.query(User).filter(User.email == user.email).first()
    db_username = db.query(User).filter(User.username == user.username).first()
    if db_email:
        raise HTTPException(status_code=400, detail="Email already exists")
    if db_username:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = generate_password_hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        is_staff=user.is_staff if user.is_staff is not None else False,
        is_active=user.is_active if user.is_active is not None else True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#login route
@auth_router.post("/login")
async def login():
    pass 