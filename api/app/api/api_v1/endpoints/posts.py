from asyncpg.exceptions import UniqueViolationError
from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, paginate
from orm.exceptions import NoMatch
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from app.models.post import Post
from app.schemas.post import PostDB, PostSchema

router = APIRouter()


@router.get("/", response_model=Page[PostDB], status_code=HTTP_200_OK)
async def get_posts():
    """Get list of of AITA posts."""
    posts = await Post.objects.all()
    return paginate(posts)


@router.post("/", response_model=PostDB, status_code=HTTP_201_CREATED)
async def add_post(payload: PostSchema):
    """Add AITA post to database."""
    try:
        return await Post.objects.create(**payload.dict())
    except UniqueViolationError as err:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Post exists") from err


@router.get("/{post_id}/", response_model=PostDB, status_code=HTTP_200_OK)
async def get_post(post_id: int):
    """Retrieve AITA post by id."""
    try:
        return await Post.objects.get(id=post_id)
    except NoMatch as err:
        raise HTTPException(HTTP_404_NOT_FOUND, "Post not found") from err


@router.put("/{post_id}/", response_model=PostDB, status_code=HTTP_200_OK)
async def update_post(post_id: int, payload: PostSchema):
    """Update attributes of AITA post."""
    post = await get_post(post_id)
    await post.update(**payload.dict())
    return await get_post(post_id)


@router.delete("/{post_id}/", response_model=PostDB, status_code=HTTP_200_OK)
async def remove_post(post_id: int):
    """Remove AITA posts by id."""
    post = await get_post(post_id)
    await post.delete()
    return post
