import uuid
from config.config import get_db_connection
from models.user import UserCreate, UserLogin
from utils.hash import hash_password, check_password

def create_user(user: UserCreate):
    user_id = str(uuid.uuid4())  # UUID 생성
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        hashed_password = hash_password(user.password)  # 비밀번호 해싱
        cursor.execute(
            "INSERT INTO users_tb (id, login_id, password, name, phone_number, gender, email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (user_id, user.login_id, hashed_password, user.name, user.phone_number, user.gender, user.email)
        )
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()

def login_user(user_login: UserLogin) -> bool:
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT id, password FROM users_tb WHERE login_id = %s", (user_login.login_id,))
        user = cursor.fetchone()

        if user is None:
            return False  # 사용자 ID가 존재하지 않음

        if not check_password(user_login.password, user["password"]):  # 비밀번호 검증
            return False  # 비밀번호 불일치

        return True  # 인증 성공
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()
