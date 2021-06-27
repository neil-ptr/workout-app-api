from pydantic import BaseModel, EmailStr


class Login(BaseModel):
    email: EmailStr
    password: str


class SignUp(BaseModel):
    email: EmailStr
    firstname: str
    password: str
    confirmPassword: str
