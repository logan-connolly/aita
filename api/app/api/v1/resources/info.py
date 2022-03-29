from collections import Counter

from fastapi import APIRouter
from starlette.requests import Request
from starlette.status import HTTP_200_OK

from app.db.tables.posts import Post
from app.schemas.reddit import PostCount, RedditInfo

router = APIRouter()


@router.get("/label/", response_model=PostCount, status_code=HTTP_200_OK)
async def get_label_counts():
    """Check how many posts are in DB for each label."""
    return Counter((post.label for post in await Post.objects.all()))


@router.get("/account/", response_model=RedditInfo, status_code=HTTP_200_OK)
async def get_connection_info(request: Request):
    """Check whether you are connected with Reddit API."""
    return {"user": request.app.state.user}
