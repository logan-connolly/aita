from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel


class LabelEnum(str, Enum):
    YTA = "YTA"
    NTA = "NTA"
    ESH = "ESH"
    NAH = "NAH"
    INFO = "INFO"
    NONE = "NONE"


# shared properties
class PostBase(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    label: Optional[Union[LabelEnum, str]] = None
    text: Optional[str] = None


# properties to receive on item creation
class PostCreate(PostBase):
    id: str
    title: str
    label: LabelEnum
    text: str


# properties to receive on item update
class PostUpdate(PostBase):
    pass


# properties shared by models stored in DB
class PostDBBase(PostBase):
    id: str
    title: str
    label: str
    text: str

    class Config:
        orm_mode = True


# properties to return to client
class PostDB(PostDBBase):
    pass
