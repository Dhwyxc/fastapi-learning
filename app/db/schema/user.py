from pydantic import BaseModel, EmailStr
from typing import Union

class UserInCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str
    address:  str
    is_active: bool = True

class UserOutput(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    address: str
    is_active: bool

class UserInUpdate(BaseModel): 
    id: int
    username: Union[str, None] = None
    email: Union[EmailStr, None] = None
    password: Union[str, None] = None
    full_name: Union[str, None] = None
    address: Union[str, None] = None
    is_active: Union[bool, None] = None

class UserInLogin(BaseModel):
    email: EmailStr
    password: str

class UserWithToken(BaseModel):
    token: str