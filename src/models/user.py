from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    login_id: str
    password: str
    name: str
    phone_number: str
    gender: str  # 'Male', 'Female', 'Other' 중 하나여야 함
    email: EmailStr


class UserLogin(BaseModel):
    login_id: str  # 로그인 ID
    password: str  # 비밀번호