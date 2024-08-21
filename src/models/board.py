from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class BoardCreate(BaseModel):
    departure_location: str
    arrival_location: str
    departure_at: datetime
    is_poll: Optional[bool] = True
    content: str

class BoardResponse(BaseModel):
    id: UUID
    departure_location: str
    arrival_location: str
    departure_at: datetime
    creator_id: str
    is_poll: bool
    votes_count: int
    comments_count: int
    created_at: datetime
    deleted_at: Optional[datetime] = None
    content: str
