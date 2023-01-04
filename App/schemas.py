'''
    BaseModel with pydantic behind that will force the rules
    This file is the objects schema, it defines the properties that the client must send in the request
    and the properties or type of the response
    
'''
#BaseModel # https://docs.pydantic.dev/
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# class to be inherited. It is the base Post properties
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# (CREATE & UPDATE) Extends/inherit PostBase- everything inherited will be accepted
class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# extends PostBase and expects more properties
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut # returns a pydantic model type userOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

# used in the authentication
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# BaseModel schema for the JWT token
class Token(BaseModel):
    access_token: str
    token_type: str

# The return schema for the JWT token
class TokenData(BaseModel):
    id: Optional[str] = None

# schema for voting object, this is what we want to show
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # zero or one anything less than 1 is allowed
