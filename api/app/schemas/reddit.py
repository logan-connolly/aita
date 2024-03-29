from enum import Enum
from typing import Optional

from pydantic import BaseModel


class SortFilter(str, Enum):
    """Time filter for fetching reddit posts"""

    hot = "hot"
    top = "top"
    new = "new"
    controversial = "controversial"


class RedditInfo(BaseModel):
    user: Optional[str] = None


class RedditLastSync(BaseModel):
    posts: int
    last_sync: str


class PostCount(BaseModel):
    YTA: Optional[int] = None
    NTA: Optional[int] = None
    ESH: Optional[int] = None
    NAH: Optional[int] = None
    NAN: Optional[int] = None
