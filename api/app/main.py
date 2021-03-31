from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .api.api_v1.routes import api_router
from .core.config import settings
from .core.event_handlers import start_app_handler, stop_app_handler


def get_app() -> FastAPI:

    app = FastAPI(
        title=settings.api.title, openapi_url=settings.api.openapi, debug=settings.DEBUG
    )

    @app.on_event("startup")
    async def startup():
        await start_app_handler(app)

    @app.on_event("shutdown")
    async def shutdown():
        await stop_app_handler(app)

    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.BACKEND_CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    app.include_router(api_router, prefix=settings.api.version)

    return app


app = get_app()
