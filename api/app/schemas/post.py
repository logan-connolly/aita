from pydantic import BaseModel

from app.core.constants import AitaLabel


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
