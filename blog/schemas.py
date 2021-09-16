from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class UserOutput(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True

class UserOutputWithList(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True

class BlogOutput(BaseModel):
    title: str
    body: str
    creator: UserOutput

    class Config():
        orm_mode = True

class UserLoginAuth(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
