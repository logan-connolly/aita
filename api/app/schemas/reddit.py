from typing import Optional

from pydantic import BaseModel


class RedditInfo(BaseModel):
    user: Optional[str] = None
