from fastapi import APIRouter

from .endpoints import posts, predict, reddit

api_router = APIRouter()

api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(predict.router, prefix="/predict", tags=["predict"])
api_router.include_router(reddit.label.router, prefix="/reddit/label", tags=["reddit"])
api_router.include_router(reddit.info.router, prefix="/reddit/info", tags=["reddit"])
api_router.include_router(reddit.sync.router, prefix="/reddit/sync", tags=["reddit"])
