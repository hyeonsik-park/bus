import uuid
from config.config import get_db_connection
from models.user import UserCreate, UserLogin


def create_user(user: UserCreate):
    user_id = str(uuid.uuid4())  # UUID 생성
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO users_tb (id, login_id, password, name, phone_number, gender, email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (user_id, user.login_id, user.password, user.name, user.phone_number, user.gender, user.email)
        )
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()


def login_user(user_login: UserLogin) -> bool:
    """
    사용자가 입력한 로그인 ID와 비밀번호를 검증하여 인증합니다.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # 로그인 ID로 사용자 정보를 조회
        cursor.execute("SELECT id, password FROM users_tb WHERE login_id = %s", (user_login.login_id,))
        user = cursor.fetchone()

        if user is None:
            return False  # 사용자 ID가 존재하지 않음

        if user_login.password != user["password"]:
            return False  # 비밀번호 불일치

        return True  # 인증 성공
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()