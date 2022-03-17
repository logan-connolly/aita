from fastapi import FastAPI

from app.core import event_handlers
from app.core.config import settings


def create_app() -> FastAPI:

    app = FastAPI(
        debug=settings.debug,
        title="Am I the asshole? (AITA)",
        description="Find out whether you are the asshole of a given story",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )

    @app.on_event("startup")
    async def startup():
        await event_handlers.start_app(app)

    @app.on_event("shutdown")
    async def shutdown():
        await event_handlers.stop_app(app)

    return app


app = create_app()
