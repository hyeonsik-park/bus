import uuid
from config.config import get_db_connection
from models.board import BoardCreate

def create_board(board: BoardCreate, creator_id: str):
    board_id = str(uuid.uuid4())  # UUID 생성
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO boards_tb (
                id, departure_location, arrival_location, departure_at,
                creator_id, is_poll, content
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                board_id,
                board.departure_location,
                board.arrival_location,
                board.departure_at,
                creator_id,
                board.is_poll,
                board.content
            )
        )
        connection.commit()
        return board_id  # 생성된 게시물의 UUID 반환
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()
