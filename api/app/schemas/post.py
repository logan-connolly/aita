from typing import Optional, Union

from pydantic import BaseModel

from app.core.constants import AitaLabel


class PostCount(BaseModel):
    YTA: Optional[int]
    NTA: Optional[int]
    ESH: Optional[int]
    NAH: Optional[int]
    INFO: Optional[int]


class PostBase(BaseModel):
    reddit_id: Optional[str] = None
    title: Optional[str] = None
    label: Optional[Union[AitaLabel, str]] = None
    text: Optional[str] = None


class PostCreate(PostBase):
    reddit_id: str
    title: str
    label: AitaLabel
    text: str


class PostDB(PostBase):
    id: int
    reddit_id: str
    title: str
    label: str
    text: str

    class Config:
        orm_mode = True
