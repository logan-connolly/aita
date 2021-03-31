from typing import Optional

from pydantic import BaseModel


class RedditInfo(BaseModel):
    user: Optional[str] = None


class RedditSync(BaseModel):
    posts: int
    new: int


class RedditLastSync(BaseModel):
    posts: int
    last_sync: str
