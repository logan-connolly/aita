from fastapi import FastAPI

from .api.api_v1.routes import api_router
from .core.config import settings
from .core.event_handlers import start_app_handler, stop_app_handler


def get_app() -> FastAPI:

    app = FastAPI(
        title=settings.API_TITLE,
        openapi_url=settings.OPENAPI_URL,
        debug=settings.DEBUG
    )

    @app.on_event("startup")
    async def startup():
        await start_app_handler(app)

    @app.on_event("shutdown")
    async def shutdown():
        await stop_app_handler(app)

    app.include_router(api_router, prefix=settings.API_V1_STR)

    return app


app = get_app()
