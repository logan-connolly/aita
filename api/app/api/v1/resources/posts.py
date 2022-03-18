from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from app.core.exceptions import DoesNotExist
from app.db.dal.posts import PostsDAL
from app.db.session import get_db
from app.schemas.post import InPostSchema, PostSchema

router = APIRouter()


@router.post("/", response_model=PostSchema, status_code=HTTP_201_CREATED)
async def add_post(payload: InPostSchema, db: AsyncSession = Depends(get_db)):
    """Add AITA reddit post to database."""
    dal = PostsDAL(db)
    try:
        return dal.create(payload)
    except IntegrityError as err:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Post exists") from err


@router.get("/{post_id}/", response_model=PostSchema, status_code=HTTP_200_OK)
async def get_post(post_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve AITA reddit post by id."""
    dal = PostsDAL(db)
    try:
        return await dal.get_by_id(post_id)
    except DoesNotExist as err:
        raise HTTPException(HTTP_404_NOT_FOUND, "Post not found") from err


@router.get("/", response_model=Page[PostSchema], status_code=HTTP_200_OK)
async def get_posts(db: AsyncSession = Depends(get_db)):
    """Get list of of AITA reddit posts."""
    dal = PostsDAL(db)
    posts = await dal.get_all()
    return paginate(posts)
