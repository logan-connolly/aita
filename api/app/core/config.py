from typing import List

from pydantic import BaseSettings


class ApiConfig(BaseSettings):
    title: str = "AITA"
    version: str = "/api/v1"
    openapi: str = "/api/v1/openapi.json"


class PostgresConfig(BaseSettings):
    user: str
    password: str
    host: str
    db: str

    class Config:
        env_prefix = "POSTGRES_"
        env_file = ".env"
        env_file_encoding = "utf-8"


class RedditConfig(BaseSettings):
    client_id: str
    client_secret: str
    password: str
    username: str

    class Config:
        env_prefix = "REDDIT_"
        env_file = ".env"
        env_file_encoding = "utf-8"


class WebSettings(BaseSettings):
    port: int

    class Config:
        env_prefix = "WEB_"
        env_file = ".env"
        env_file_encoding = "utf-8"


class Settings(BaseSettings):
    api = ApiConfig()
    pg = PostgresConfig()
    reddit = RedditConfig()
    web = WebSettings()

    DEBUG: bool = True
    MODEL_PATH: str = "example/path"
    URI: str = f"postgresql://{pg.user}:{pg.password}@{pg.host}/{pg.db}"
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost",
        f"http://localhost:{web.port}",
    ]

    class Config:
        case_sensitive = True


settings = Settings()
