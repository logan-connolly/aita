from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app import models
from app.schemas.reddit import RedditLastSync, RedditSync
from app.services.reddit import extract_post_info

router = APIRouter()


@router.get("/", response_model=RedditLastSync, status_code=HTTP_200_OK)
async def get_last_sync():
    """Get information on the last sync and number of posts in DB."""
    posts = await models.Post.objects.all()
    if not posts:
        raise HTTPException(HTTP_404_NOT_FOUND, "No posts found in DB")

    latest_post = max(post.ts for post in posts)
    return {"posts": len(posts), "last_sync": latest_post.strftime("%Y-%m-%d %H:%M")}


@router.post("/", response_model=RedditSync, status_code=HTTP_201_CREATED)
async def sync_reddit_posts(request: Request, limit: int = 10):
    """Pull subreddit submissions from Reddit and process them accordingly."""

    subreddit = await request.app.state.reddit.subreddit("AmItheAsshole")
    saved_post_ids = {post.reddit_id for post in await models.Post.objects.all()}
    new_posts = 0

    async for raw_post in subreddit.top(limit=limit):
        post = await extract_post_info(raw_post)

        if post.label is None:
            continue

        if post.reddit_id in saved_post_ids:
            stored_post = await models.Post.objects.get(reddit_id=post.reddit_id)
            await stored_post.update(**post.dict())
        else:
            new_posts += 1
            await models.Post.objects.create(**post.dict())

    return {"posts": len(saved_post_ids) + new_posts, "new": new_posts}
