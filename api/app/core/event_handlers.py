from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.db.database import database
from app.core.config import settings
from app.services.model import AITAClassifier


async def start_app_handler(app: FastAPI) -> Callable:
    model = AITAClassifier(settings.MODEL_PATH)
    app.state.model = model
    logger.info(f"{model} loaded and attached to app.")
    await database.connect()


async def stop_app_handler(app: FastAPI) -> Callable:
    app.state.model = None
    await database.disconnect()
