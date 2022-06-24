import uuid

from app.core.constants import AitaLabel
from app.schemas.base import BaseSchema


class PostSchemaBase(BaseSchema):
    id: uuid.UUID
    text: str
    title: str


class InPostSchema(PostSchemaBase):
    label: AitaLabel


class PostSchema(PostSchemaBase):
    label: str
