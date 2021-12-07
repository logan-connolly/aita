from collections import Counter

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from app.models.post import Post
from app.schemas.post import PostCount

router = APIRouter()


@router.get("/", response_model=PostCount, status_code=HTTP_200_OK)
async def get_label_counts():
    """Check how many posts are in DB for each label."""
    posts = await Post.objects.all()
    if not posts:
        raise HTTPException(HTTP_404_NOT_FOUND, "No posts found in DB")

    counter = Counter()
    for post in posts:
        counter[post.label] += 1

    return dict(counter)
