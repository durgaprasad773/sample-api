from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, EmailStr
from typing import List
from datetime import timedelta

from models import Base, User
from auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    verify_token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sample API", description="API with login and protected routes")

# Pydantic models
class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    name: str
    phone: str
    email: str

    class Config:
        from_attributes = True

class ProductResponse(BaseModel):
    productId: str
    name: str
    price: int
    inStock: bool
    category: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Welcome to the API. Use /login to authenticate, and /products to view product data."}

@app.post("/login", response_model=Token)
def login(user_credentials: UserLogin):
    # Hardcoded credentials
    VALID_USERNAME = "rahul"
    VALID_PASSWORD = "rahul@2021"
    
    if user_credentials.username != VALID_USERNAME or user_credentials.password != VALID_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": VALID_USERNAME}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/products", response_model=List[ProductResponse])
def get_projects(username: str = Depends(verify_token)):
    # Verify the authenticated user
    if username != "rahul":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    # Return sample product data
    products = [
        {
            "productId": "P101",
            "name": "Laptop",
            "price": 55000,
            "inStock": True,
            "category": "Electronics"
        },
        {
            "productId": "P102",
            "name": "Headphones",
            "price": 2500,
            "inStock": False,
            "category": "Accessories"
        },
        {
            "productId": "P103",
            "name": "Smartwatch",
            "price": 9999,
            "inStock": True,
            "category": "Wearables"
        }
    ]
    return products
