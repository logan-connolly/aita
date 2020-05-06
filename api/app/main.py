from fastapi import FastAPI

from .api.api_v1.routes import api_router
from .core.config import settings
from .db.database import database, engine, metadata
from .services.model import AITAClassifier


def get_app():
    app = FastAPI(title="AITA", openapi_url=f"{settings.API_V1_STR}/openapi.json")

    metadata.create_all(engine)

    @app.on_event("startup")
    async def startup():
        model = AITAClassifier(settings.MODEL_PATH)
        app.state.model = model
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        app.state.model = None
        await database.disconnect()

    app.include_router(api_router, prefix=settings.API_V1_STR)

    return app


app = get_app()
