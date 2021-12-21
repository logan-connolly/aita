from typing import Optional

from pydantic import BaseModel

from app.core.constants import AitaLabel


class PostCount(BaseModel):
    YTA: Optional[int]
    NTA: Optional[int]
    ESH: Optional[int]
    NAH: Optional[int]
    INFO: Optional[int]


class PostSchema(BaseModel):
    reddit_id: str
    title: str
    label: AitaLabel
    text: str


class PostDB(BaseModel):
    id: int
    reddit_id: str
    title: str
    label: str
    text: str

    class Config:
        orm_mode = True
