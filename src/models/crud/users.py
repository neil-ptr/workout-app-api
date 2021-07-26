from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    firstname: str


class UserCreate(UserBase):
    hash: str
