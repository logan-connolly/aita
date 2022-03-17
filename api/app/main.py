from fastapi import FastAPI

from app.core.config import settings
from app.core.event_handlers import start_app_handler, stop_app_handler


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
        await start_app_handler(app)

    @app.on_event("shutdown")
    async def shutdown():
        await stop_app_handler(app)

    return app


app = create_app()
