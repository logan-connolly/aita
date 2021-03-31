from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from app.schemas.reddit import RedditLastSync, RedditSync

router = APIRouter()


@router.get("/", response_model=RedditLastSync, status_code=HTTP_200_OK)
async def get_last_sync():
    """Get information on the last sync"""
    return {"posts": 10, "last_sync": "2020-08-09"}


@router.post("/", response_model=RedditSync, status_code=HTTP_201_CREATED)
async def sync_reddit_posts():
    """Check whether you are connected with Reddit API."""
    return {"posts": 10, "new": 5}
