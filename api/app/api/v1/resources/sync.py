from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.requests import Request
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.core.constants import AITA_SUBREDDIT_NAME
from app.core.exceptions import DoesNotExist
from app.core.services.reddit import extract_post_info
from app.db.dal.posts import PostsDAL
from app.db.session import get_db
from app.schemas.reddit import RedditLastSync, SortFilter

router = APIRouter()


@router.get("/", response_model=RedditLastSync, status_code=HTTP_200_OK)
async def get_last_sync(db: AsyncSession = Depends(get_db)):
    """Get information on the last sync and number of posts in DB."""
    posts = await PostsDAL(db).get_all()
    if not posts:
        raise HTTPException(HTTP_404_NOT_FOUND, "No posts found in DB")

    latest_post = max(post.ts for post in posts)
    return {"posts": len(posts), "last_sync": latest_post.strftime("%Y-%m-%d %H:%M")}


@router.post("/", response_model=RedditLastSync, status_code=HTTP_201_CREATED)
async def sync_reddit_posts(
    request: Request,
    filter: SortFilter = SortFilter.hot,
    limit: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
):
    """Pull subreddit submissions from Reddit and process them accordingly."""
    subreddit = await request.app.state.reddit.subreddit(AITA_SUBREDDIT_NAME)
    dal = PostsDAL(db)

    async for raw_post in getattr(subreddit, filter)(limit=limit):
        extracted_post = await extract_post_info(raw_post)
        try:
            await dal.get_by_id(extracted_post.id)
        except DoesNotExist:
            await dal.create(extracted_post)

    posts = await dal.get_all()
    return {"posts": len(posts), "last_sync": datetime.now().strftime("%Y-%m-%d %H:%M")}
