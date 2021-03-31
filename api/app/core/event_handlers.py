from fastapi import FastAPI
from loguru import logger

from app.core.config import settings
from app.db.database import database
from app.services.model import AITAClassifier
from app.services.reddit import get_reddit_connection


async def start_app_handler(app: FastAPI) -> None:
    app.state.model = AITAClassifier(settings.MODEL_PATH)
    app.state.reddit = get_reddit_connection(settings.reddit)
    await database.connect()


async def stop_app_handler(app: FastAPI) -> None:
    app.state.model = None
    app.state.reddit = None
    await database.disconnect()
