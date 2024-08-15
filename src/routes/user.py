from fastapi import APIRouter, HTTPException
from services.user import create_user, login_user
from models.user import UserCreate, UserLogin


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
    """
    사용자 로그인 엔드포인트.
    """
    is_authenticated = login_user(user)

    if not is_authenticated:
        # 인증 실패 시 HTTP 401 오류 반환
        raise HTTPException(status_code=401, detail="아이디 또는 비밀번호가 유효하지 않습니다.")

    return {"message": "로그인 성공했습니다."}  # 성공 메시지 반환