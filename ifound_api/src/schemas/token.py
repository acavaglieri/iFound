from typing import Optional
from pydantic import BaseModel
from ..schemas import users as u_schemas

class Token(BaseModel):
    access_token: str
    token_type: str
    user: u_schemas.UserLoginResponse
    status: str
    message: str

class TokenData(BaseModel):
    username: Optional[str] = None