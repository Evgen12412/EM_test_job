import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class ResponseBase(BaseModel):
    model_config = ConfigDict(
        json_encoders={
            datetime.datetime: lambda v: v.timestamp(),
        },
    )


class BookResponse(ResponseBase):
    id: int
    title: str
    author: str
    year: datetime.datetime
    status: str


class BookListResponse(ResponseBase):
    items: List[BookResponse]


class BookCreateRequest(BaseModel):
    title: str
    author: Optional[str] = None
    year: Optional[datetime.datetime] = None
    status: Optional[str] = None


class BookCreateResponse(ResponseBase):
    id: int


class BookUpdateRequest(BaseModel):
    title: str
    author: Optional[str] = None
    year: Optional[datetime.datetime] = None
    status: Optional[str] = None


class BookUpdateResponse(ResponseBase):
    id: int


class BookDeleteResponse(ResponseBase):
    id: int
