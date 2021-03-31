from fastapi import APIRouter

from .endpoints import posts, predict
from .endpoints.reddit import info

api_router = APIRouter()

api_router.include_router(info.router, prefix="/reddit/info", tags=["reddit", "info"])
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(predict.router, prefix="/predict", tags=["predict"])
