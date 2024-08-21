from fastapi import APIRouter, Depends, HTTPException
from services.board import create_board
from models.board import BoardCreate, BoardResponse
from routes.dependencies import get_current_user
from datetime import datetime

router = APIRouter()

@router.post("/board", response_model=BoardResponse)
async def create_new_board(board: BoardCreate, creator_id: str = Depends(get_current_user)):
    try:
        board_id = create_board(board, creator_id)
        return BoardResponse(
            id=board_id,
            departure_location=board.departure_location,
            arrival_location=board.arrival_location,
            departure_at=board.departure_at,
            creator_id=creator_id,
            is_poll=board.is_poll,
            votes_count=0,
            comments_count=0,
            created_at=datetime.utcnow(),
            content=board.content
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail="게시물 생성 실패: " + str(e))
