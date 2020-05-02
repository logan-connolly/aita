from typing import Optional

from pydantic import BaseModel


# shared properties
class PostBase(BaseModel):
    post_id: Optional[str] = None
    label: Optional[str] = None
    text: Optional[str] = None


# properties to receive on item creation
class PostCreate(BaseModel):
    post_id: str
    label: str
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
