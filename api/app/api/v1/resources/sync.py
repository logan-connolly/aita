from typing import Optional

from fastapi import APIRouter, HTTPException
from orm.exceptions import NoMatch
from starlette.requests import Request
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.core.constants import AITA_SUBREDDIT_NAME
from app.core.services.reddit import extract_post_info
from app.db.tables.posts import Post
from app.schemas.reddit import RedditLastSync, SortFilter

router = APIRouter()


@router.get("/", response_model=RedditLastSync, status_code=HTTP_200_OK)
async def get_last_sync():
    """Get information on the last sync and number of posts in DB."""
    posts = await Post.objects.all()
    if not posts:
        raise HTTPException(HTTP_404_NOT_FOUND, "No posts found in DB")

    latest_post = max(post.ts for post in posts)
    return {"posts": len(posts), "last_sync": latest_post.strftime("%Y-%m-%d %H:%M")}


@router.post("/", response_model=RedditLastSync, status_code=HTTP_201_CREATED)
async def sync_reddit_posts(
    request: Request, filter: SortFilter = SortFilter.hot, limit: Optional[int] = None
):
    """Pull subreddit submissions from Reddit and process them accordingly."""

    subreddit = await request.app.state.reddit.subreddit(AITA_SUBREDDIT_NAME)

    async for raw_post in getattr(subreddit, filter)(limit=limit):
        post = await extract_post_info(raw_post)
        try:
            stored_post = await Post.objects.get(reddit_id=post.reddit_id)
            await stored_post.update(**post.dict())
        except NoMatch:
            await Post.objects.create(**post.dict())

    return await get_last_sync()
