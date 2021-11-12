from fastapi import FastAPI

from app.api.api_v1.routes import api_router
from app.core.config import settings
from app.core.middleware import add_cors_middleware
from app.db.database import database
from app.services.model import AITAClassifier
from app.services.reddit import get_reddit_connection, get_reddit_user


async def start_app_handler(app: FastAPI) -> None:
    """Services to start upon app launch"""

    app.state.model = AITAClassifier(settings.MODEL_PATH)
    app.state.reddit = await get_reddit_connection(settings.reddit)
    app.state.user = await get_reddit_user(app.state.reddit)

    app.include_router(api_router, prefix=settings.api.version)
    add_cors_middleware(app)

    await database.connect()


async def stop_app_handler(app: FastAPI) -> None:
    """Services to stop upon app shutdown"""
    app.state.model = None
    app.state.reddit = None
    await database.disconnect()
