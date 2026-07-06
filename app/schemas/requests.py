from datetime import datetime
from pydantic import BaseModel

from app.enums.request import RequestStatus


class RequestCreate(BaseModel):
    donation_id: int


class RequestResponse(BaseModel):
    id: int
    donation_id: int
    ngo_id: int
    status: RequestStatus
    requested_at: datetime

    class Config:
        from_attributes = True