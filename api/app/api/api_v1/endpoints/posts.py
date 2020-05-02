from typing import List

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
async def get_posts(label: str = None):
    posts = await (
        models.Post.objects.filter(label__contains=label).all()
        if label
        else models.Post.objects.all()
    )
    if not posts:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No posts found")
    return posts


@router.post("/", response_model=schemas.PostDB, status_code=HTTP_201_CREATED)
async def add_post(payload: schemas.PostCreate):
    try:
        return await models.Post.objects.create(**vars(payload))
    except UniqueViolationError:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Post exists")


@router.get("/{id}/", response_model=schemas.PostDB, status_code=HTTP_200_OK)
async def get_post(id: int):
    try:
        return await models.Post.objects.get(id=id)
    except NoMatch:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not found")


@router.put("/{id}/", response_model=schemas.PostDB, status_code=HTTP_200_OK)
async def update_post(id: int, payload: schemas.PostUpdate):
    post = await get_post(id)
    await post.update(**vars(payload))
    return post


@router.delete("/{id}/", response_model=schemas.PostDB, status_code=HTTP_200_OK)
async def remove_post(id: int):
    post = await get_post(id)
    await post.delete()
    return post
