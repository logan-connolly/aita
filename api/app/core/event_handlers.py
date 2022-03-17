from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.api.api_v1.routes import api_router
from app.core.config import settings
from app.core.services.classifiers.dummy import DummyClassifier
from app.core.services.predict import AitaPredictor
from app.core.services.reddit import get_reddit_connection, get_reddit_user


async def start_app(app: FastAPI) -> None:
    """Services to start upon app launch"""

    app.state.model = AitaPredictor(classifier=DummyClassifier())
    app.state.reddit = await get_reddit_connection(settings.reddit)
    app.state.user = await get_reddit_user(app.state.reddit)

    app.include_router(api_router, prefix=settings.api_version)
    add_pagination(app)


async def stop_app(app: FastAPI) -> None:
    """Services to stop upon app shutdown"""
    await app.state.reddit.close()
