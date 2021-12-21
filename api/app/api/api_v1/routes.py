from fastapi import APIRouter

from .endpoints import info, posts, predict, sync

api_router = APIRouter()

api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(predict.router, prefix="/predict", tags=["predict"])
api_router.include_router(info.router, prefix="/info", tags=["info"])
api_router.include_router(sync.router, prefix="/sync", tags=["sync"])
