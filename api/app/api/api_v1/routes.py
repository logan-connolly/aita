from fastapi import APIRouter

from .endpoints import posts, predict

api_router = APIRouter()
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(predict.router, prefix="/predict", tags=["predict"])
