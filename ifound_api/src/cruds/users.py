import os
from sqlalchemy.orm import Session, session
from src.services import email_messages
from sqlalchemy import update, or_
from sqlalchemy.sql.expression import asc, desc
from src.models import user as u_model
from src.schemas import users as u_schemas
from datetime import datetime
from src.resources import authentication as auth
import traceback
import hashlib


def get_user_by_id(db: Session, user_id: int):
    return db.query(u_model.User).filter(u_model.User.id == user_id).first()

def get_user_by_federal_id(db: Session, federal_id: str):
    return db.query(u_model.User).filter(u_model.User.federal_id == federal_id).first()

def get_user_by_email(db: Session, email: str):
    query = db.query(u_model.User).filter(u_model.User.email == email)
    result = query.first()
    return result
 
def get_user_by_phone(db: Session, phone: str):
    return db.query(u_model.User).filter(u_model.User.cellphone == phone).first()

def get_user_email_by_token(db: Session, token: str):
    return db.query(u_model.User).filter(u_model.User.token == token).first()

def get_users(db: Session, filter: u_schemas.UsersFilter):
    conditions = []
    limit = None
    skip = filter.skip
    order = asc

    if filter.id:
        conditions.append(u_model.User.id == filter.id)
    if filter.name:
        conditions.append(u_model.User.name.like(f'%{filter.name}%'))
    if filter.email:
        conditions.append(u_model.User.email.like(f'%{filter.email}%'))
    if filter.cellphone:
        conditions.append(u_model.User.cellphone == filter.cellphone)
    if filter.federal_id:
        conditions.append(u_model.User.federal_id.like(f'%{filter.federal_id}%'))
    if filter.is_inactive:
        conditions.append(u_model.User.is_inactive == filter.is_inactive)
    if filter.full_search:
        conditions.append(or_(u_model.User.name.like(f'%{filter.full_search}%'), u_model.User.email.like(f'%{filter.full_search}%')))
    if filter.limit:
        limit = int(filter.limit)
    
    db_query = db.query(u_model.User)

    for i in range(len(conditions)):
        db_query = db_query.filter(conditions[i])

    db_users_total_count = db_query.count()

    if filter.sort:
        if filter.order == False:
            order = asc
        elif filter.order == True:
            order = desc

        db_query = db_query.order_by(order(filter.sort)).limit(limit).offset(skip)
        return db_query.all(), db_users_total_count

    else:
        db_query = db_query.limit(limit).offset(skip)
        return db_query.all(), db_users_total_count

def register_user(db: Session, user: u_schemas.UserCreate):
    #hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    hashed_password = auth.get_password_hash(user.password)
    user_dict = user.dict()
    del user_dict['password']
    del user_dict['status']
    del user_dict['message']
    user_dict['created_at'] = datetime.today()
    user_dict['updated_at'] = datetime.today()
    db_user = u_model.User(**user_dict, encrypted_password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(u_model.User)\
        .filter(u_model.User.id == user_id)\
            .first()
    db.delete(db_user)
    db.commit()

def update_user(db: Session, user: u_schemas.UserUpdate, user_id: int):
    db_user = update(u_model.User)\
        .where(u_model.User.id == user_id)\
            .values(**user.dict(exclude_unset=True))
    db.execute(db_user)
    db.commit()

def auth_user(db: Session, user_login: u_schemas.UserLoginRequest):
    #hashed_password = hashlib.sha256(user_login.password.encode()).hexdigest()
    hashed_password = auth.get_password_hash(user_login.password)
    db_user = get_user_by_email(db, email=user_login.email)
    if db_user and db_user.encrypted_password == hashed_password:
        return db_user  
    return False

def generate_email_data(user, message_type):
    today = datetime.today()
    token = hashlib.sha256(str(today).encode()).hexdigest()
    user_name = user.name.split()
    url_link = os.environ["URL_LINK"]
    message = email_messages.html_message(message_type, url_link, user_name[0], token)
    email_data = {
    "token": token,
    "message": message,
    }
    return email_data

def insert_user_token(db: Session, user_email: u_schemas.UserResetPassEmail, token: str):
    db_user = update(u_model.User)\
        .where(u_model.User.email == user_email)\
            .values(token=token)
    db_user = db.execute(db_user)
    db.commit()
    return db_user

def confirm_user(db: Session, token: u_schemas.UserToken):
    db_user = update(u_model.User)\
        .where(u_model.User.token == token.token)\
            .values(is_confirmed=True, token=None)
    db.execute(db_user)
    db.commit()

def user_reset_password(db: Session, user: u_schemas.UserResetPass, token: u_schemas.UserToken):
    db_user = get_user_by_email(db, user.email)
    if db_user and db_user.token == token.token and user.new_password:
        new_pass_user = update(u_model.User)\
        .where(u_model.User.token == token.token)\
        .values(encrypted_password=hashlib.sha256(user.new_password.encode()).hexdigest(), token=None)
        db.execute(new_pass_user)
        db.commit()
        return db_user