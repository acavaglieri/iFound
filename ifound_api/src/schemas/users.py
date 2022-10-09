from datetime import datetime
from typing import Optional, List
from src.schemas.status import StatusModel, BaseModel


class UserBase(StatusModel):
    name: str
    email: str
    cellphone: str
    federal_id: str
    is_confirmed: bool
    is_inactive: Optional[bool] = False
    role: str

class UserCreate(UserBase):
    password: str

class UserCreatePersist(UserCreate):
    encrypted_password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
	    orm_mode=True

class UserByToken(StatusModel):
    email: Optional[str]

class UsersFilter(StatusModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    cellphone: Optional[str] = None
    federal_id: Optional[str] = None
    is_inactive: Optional[bool] = False
    skip: Optional[int] = None
    limit: Optional[int] = None
    full_search: Optional[str] = None
    order: Optional[bool] = None
    sort: Optional[str] = None

class UserUpdate(StatusModel):
    name: Optional[str] = None
    email: Optional[str] = None
    cellphone: Optional[str] = None
    role: Optional[str] = None
    federal_id: Optional[str] = None
    updated_at: datetime = datetime.today()

class AllUsers(StatusModel):
    users_total_count: int
    users: List[User]
    
    class Config:
        orm_mode=True

class UserLoginRequest(StatusModel):
    email: str
    password: str
    class Config:
        orm_mode=True

class UserLoginResponse(BaseModel):
    email: str = None
    role: str = None

class UserResetPassEmail(StatusModel):
    email: str

class UserResetPass(StatusModel):
    email: str
    new_password: str

class UserToken(StatusModel):
    token: str

