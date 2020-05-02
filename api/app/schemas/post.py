from enum import Enum
from typing import Optional

from pydantic import BaseModel


class LabelEnum(str, Enum):
    YTA = "YTA"
    NTA = "NTA"
    ESH = "ESH"
    NAH = "NAH"
    INFO = "INFO"


# shared properties
class PostBase(BaseModel):
    post_id: Optional[str] = None
    label: Optional[LabelEnum] = None
    text: Optional[str] = None


# properties to receive on item creation
class PostCreate(BaseModel):
    post_id: str
    label: LabelEnum
    text: str


# properties to receive on item update
class PostUpdate(PostBase):
    pass


# properties hared by models stored in DB
class PostDBBase(PostBase):
    id: int
    post_id: str
    label: str
    text: str

    class Config:
        orm_mode = True


# properties to return to client
class PostDB(PostDBBase):
    pass
