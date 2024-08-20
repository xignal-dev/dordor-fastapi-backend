from pydantic import BaseModel, UUID4, Field, EmailStr
from datetime import date, datetime


class UserInput(BaseModel):
  # id: int
  address: str
  email: EmailStr
  # password: str
  # salt: str
  nickname: str
  mobile: str
  
  bio: str
  telegram: str
  twitter: str
  instagram: str
  discord: str
  # is_valid: bool
  
class UserOutput(BaseModel):
  id: int
  address: str | None = None
  email: EmailStr | None = None
  # password: str
  # salt: str
  nickname: str | None = None
  mobile: str | None = None
  
  bio: str | None = None
  telegram: str | None = None
  twitter: str | None = None
  instagram: str| None = None
  discord: str | None = None
  is_valid: bool | None = None
  
  created_at: datetime | None = None
  modified_at: datetime | None = None
  
class UserInDb(BaseModel):
  id: int
  address: str | None = None
  email: EmailStr | None = None
  # password: str
  # salt: str
  nickname: str | None = None
  mobile: str | None = None
  
  bio: str | None = None
  telegram: str | None = None
  twitter: str | None = None
  instagram: str | None = None
  discord: str | None = None
  is_valid: bool | None = None
  
  created_at: datetime
  modified_at: datetime
  
  class Config:
    orm_mode = True