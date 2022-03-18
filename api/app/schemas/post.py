from app.core.constants import AitaLabel
from app.schemas.base import BaseSchema


class PostSchemaBase(BaseSchema):
    reddit_str: str
    text: str
    title: str


class InPostSchema(PostSchemaBase):
    label: AitaLabel


class PostSchema(PostSchemaBase):
    id: int
    label: str
