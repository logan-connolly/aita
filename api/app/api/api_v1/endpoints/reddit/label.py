from collections import Counter

from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from app.models.post import Post
from app.schemas.reddit import PostCount

router = APIRouter()


@router.get("/", response_model=PostCount, status_code=HTTP_200_OK)
async def get_label_counts():
    """Check how many posts are in DB for each label."""
    return Counter((post.label for post in await Post.objects.all()))
