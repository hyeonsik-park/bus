from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from utils.jwt import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="인증 정보가 유효하지 않습니다.")
    return payload["sub"]  # user_id 반환
