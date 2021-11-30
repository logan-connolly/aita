from fastapi import FastAPI

from app.api.api_v1.routes import api_router
from app.core.config import settings
from app.core.middleware import add_cors_middleware
from app.core.services.classifiers.dummy import DummyClassifier
from app.core.services.predict import AitaPredictor
from app.core.services.reddit import get_reddit_connection, get_reddit_user
from app.db.database import database


async def start_app_handler(app: FastAPI) -> None:
    """Services to start upon app launch"""

    classifier = DummyClassifier()

    app.state.model = AitaPredictor(classifier=classifier)
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
