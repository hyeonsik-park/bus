from fastapi import APIRouter, HTTPException
from services.user import create_user, login_user
from models.user import UserCreate, UserLogin
from utils.jwt import create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate):
    try:
        create_user(user)
        return {"message": "회원가입이 완료되었습니다."}
    except Exception as e:
        raise HTTPException(status_code=400, detail="회원가입 실패: " + str(e))

@router.post("/login")
async def login(user: UserLogin):
    is_authenticated = login_user(user)
    if not is_authenticated:
        raise HTTPException(status_code=401, detail="아이디 또는 비밀번호가 유효하지 않습니다.")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.login_id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
