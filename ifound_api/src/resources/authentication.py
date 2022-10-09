from jose import JWTError, jwt
import asyncio
from sqlalchemy.orm import Session
from ..cruds import users as users_crud
from ..schemas import token as token_schema
from ..schemas import users as users_schema
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from passlib.context import CryptContext
from src.database.database  import *
import os

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

authorization_exception = HTTPException(
    status_code=401,
    detail="Você não possui autorização para executar esta ação"
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db, email: str, password: str):
    user = users_crud.get_user_by_email(db=db, email=email)
    if not user:
        return False
    if not verify_password(password, user.encrypted_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.environ["SECRET_KEY"], algorithm=os.environ["ALGORITHM"])
    return encoded_jwt

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Credenciais Inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.environ["SECRET_KEY"], algorithms=[os.environ["ALGORITHM"]])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = token_schema.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = users_crud.get_user_by_email(db=db, email=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user: users_schema.User = Depends(get_current_user)):
    if current_user.is_inactive:
        raise HTTPException(status_code=400, detail="Usuários Inativo")
    return current_user

def valid_ability_user(current_user: users_schema.User = Depends(get_current_user)):
    if current_user.role != 'admin':
        raise authorization_exception
    return current_user