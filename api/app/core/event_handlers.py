import debugpy
from fastapi import FastAPI
from loguru import logger

from app.core.config import settings
from app.db.database import database
from app.services.model import AITAClassifier
from app.services.reddit import get_reddit_connection, get_reddit_user


async def start_app_handler(app: FastAPI) -> None:
    """Services to start upon app launch"""
    if settings.DEBUG:
        logger.info("Debugpy server starting on port 5678")
        debugpy.listen(("0.0.0.0", 5678))

    app.state.model = AITAClassifier(settings.MODEL_PATH)
    app.state.reddit = await get_reddit_connection(settings.reddit)
    app.state.user = await get_reddit_user(app.state.reddit)
    await database.connect()


async def stop_app_handler(app: FastAPI) -> None:
    """Services to stop upon app shutdown"""
    app.state.model = None
    app.state.reddit = None
    await database.disconnect()
