import random
from typing import Any, Dict, List

from asyncpg.exceptions import UniqueViolationError
from fastapi import APIRouter, HTTPException
from orm.exceptions import NoMatch
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from app import models, schemas


router = APIRouter()


@router.get("/", response_model=List[schemas.PostDB], status_code=HTTP_200_OK)
async def get_posts(label: str = None, n: int = 5):
    """Get list of of AITA posts.
    :param label: filter by AITA label
    :param n: limit the number of posts returned
    """
    posts = await models.Post.objects.all()
    if not posts:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No posts found")
    if label:
        posts = [post for post in posts if post.label == label]
    sample_size = min(len(posts), n)
    return random.sample(posts, sample_size)


@router.post("/", response_model=schemas.PostDB, status_code=HTTP_201_CREATED)
async def add_post(payload: schemas.PostCreate):
    """Add AITA post to database.
    :param payload: id, label, text, title
    """
    try:
        await models.Post.objects.create(**payload.dict())
        return payload
    except UniqueViolationError:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Post exists")


@router.get("/{id}/", response_model=schemas.PostDB, status_code=HTTP_200_OK)
async def get_post(id: str):
    """Retrieve AITA post by id.
    :param id: id assigned to AITA post by reddit
    """
    try:
        return await models.Post.objects.get(id=id)
    except NoMatch:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not found")


@router.put("/{id}/", response_model=schemas.PostDB, status_code=HTTP_200_OK)
async def update_post(id: str, payload: schemas.PostUpdate):
    """Update attributes of AITA post.
    :param id: id assigned to AITA post by reddit
    :param payload:
    """
    post = await get_post(id)
    updates: Dict[str, Any] = {k: v for k, v in payload.dict().items() if v is not None}
    await post.update(**updates)
    return post


@router.delete("/{id}/", response_model=schemas.PostDB, status_code=HTTP_200_OK)
async def remove_post(id: str):
    """Remove AITA posts by id.
    :param id: id assigned to AITA post by reddit
    """
    post = await get_post(id)
    await post.delete()
    return post
