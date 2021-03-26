from typing import List

from pydantic import BaseSettings


class PostgresSettings(BaseSettings):
    user: str
    password: str
    host: str
    db: str

    class Config:
        env_prefix = "POSTGRES_"


class WebSettings(BaseSettings):
    port: int

    class Config:
        env_prefix = "WEB_"


class Settings(BaseSettings):
    pg = PostgresSettings()
    web = WebSettings()

    DEBUG: bool = True

    API_TITLE: str = "AITA"
    API_V1_STR: str = "/api/v1"
    OPENAPI_URL: str = f"{API_V1_STR}/openapi.json"

    MODEL_PATH: str = "example/path"

    URI: str = f"postgresql://{pg.user}:{pg.password}@{pg.host}/{pg.db}"

    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost",
        f"http://localhost:{web.port}",
    ]

    class Config:
        case_sensitive = True


settings = Settings()
