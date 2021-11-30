import random

from asyncpg.exceptions import UniqueViolationError
from fastapi import APIRouter, HTTPException
from orm.exceptions import NoMatch
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from app.models.post import Post
from app.schemas.post import PostBase, PostCreate, PostDB

router = APIRouter()


@router.get("/", response_model=list[PostDB], status_code=HTTP_200_OK)
async def get_posts(label: str = None, limit: int = None):
    """Get list of of AITA posts.

    label (str): filter by AITA label
    limit (str): limit the number of posts returned
    """
    posts = await Post.objects.all()

    if not posts:
        raise HTTPException(HTTP_404_NOT_FOUND, "No posts found")

    n_posts = len(posts)

    if label:
        posts = [post for post in posts if post.label == label]
    if limit:
        n_posts = limit if limit < n_posts else n_posts

    return random.sample(posts, n_posts)


@router.post("/", response_model=PostDB, status_code=HTTP_201_CREATED)
async def add_post(payload: PostCreate):
    """Add AITA post to database."""
    try:
        await Post.objects.create(**payload.dict())
        return payload
    except UniqueViolationError as err:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Post exists") from err


@router.get("/{post_id}/", response_model=PostDB, status_code=HTTP_200_OK)
async def get_post(post_id: str):
    """Retrieve AITA post by id."""
    try:
        return await Post.objects.get(id=post_id)
    except NoMatch as err:
        raise HTTPException(HTTP_404_NOT_FOUND, "Post not found") from err


@router.put("/{post_id}/", response_model=PostDB, status_code=HTTP_200_OK)
async def update_post(post_id: str, payload: PostBase):
    """Update attributes of AITA post."""
    post = await get_post(post_id)
    updates: dict[str, str] = {k: v for k, v in payload.dict().items() if v is not None}
    await post.update(**updates)
    return await get_post(post_id)


@router.delete("/{post_id}/", response_model=PostDB, status_code=HTTP_200_OK)
async def remove_post(post_id: str):
    """Remove AITA posts by id."""
    post = await get_post(post_id)
    await post.delete()
    return post
