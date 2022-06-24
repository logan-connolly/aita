from collections import Counter

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.requests import Request
from starlette.status import HTTP_200_OK

from app.db.dal.posts import PostsDAL
from app.db.session import get_db
from app.schemas.reddit import PostCount, RedditInfo

router = APIRouter()


@router.get("/label/", response_model=PostCount, status_code=HTTP_200_OK)
async def get_label_counts(db: AsyncSession = Depends(get_db)):
    """Check how many posts are in DB for each label."""
    posts = await PostsDAL(db).get_all()
    return Counter(post.label for post in posts)


@router.get("/account/", response_model=RedditInfo, status_code=HTTP_200_OK)
async def get_connection_info(request: Request):
    """Check whether you are connected with Reddit API."""
    return {"user": request.app.state.user}
