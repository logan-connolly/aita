from fastapi import APIRouter

from app.api.v1 import resources

api_router = APIRouter()

api_router.include_router(resources.posts.router, prefix="/posts")
api_router.include_router(resources.predict.router, prefix="/predict")
api_router.include_router(resources.info.router, prefix="/info")
api_router.include_router(resources.sync.router, prefix="/sync")
