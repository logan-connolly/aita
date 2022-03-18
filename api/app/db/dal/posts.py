from typing import Type

from app.db.dal.base import BaseDAL
from app.db.tables.posts import Post
from app.schemas.post import InPostSchema, PostSchema


class PostsDAL(BaseDAL[InPostSchema, PostSchema, Post]):
    """Data abstraction layer for interacting with Post objects"""

    @property
    def _schema(self) -> Type[PostSchema]:
        return PostSchema

    @property
    def _table(self) -> Type[Post]:
        return Post
