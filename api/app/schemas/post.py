from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel


class LabelEnum(str, Enum):
    YTA = "YTA"
    NTA = "NTA"
    ESH = "ESH"
    NAH = "NAH"
    INFO = "INFO"


class PostCount(BaseModel):
    YTA: Optional[int]
    NTA: Optional[int]
    ESH: Optional[int]
    NAH: Optional[int]
    INFO: Optional[int]


class PostBase(BaseModel):
    reddit_id: Optional[str] = None
    title: Optional[str] = None
    label: Optional[Union[LabelEnum, str]] = None
    text: Optional[str] = None


class PostCreate(PostBase):
    reddit_id: str
    title: str
    label: LabelEnum
    text: str


class PostUpdate(PostBase):
    pass


class PostDB(PostBase):
    id: int
    reddit_id: str
    title: str
    label: str
    text: str

    class Config:
        orm_mode = True
