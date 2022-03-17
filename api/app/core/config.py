from pydantic import BaseSettings


class PostgresConfig(BaseSettings):
    user: str
    password: str
    host: str
    db: str

    class Config:
        env_prefix = "POSTGRES_"


class RedditConfig(BaseSettings):
    client_id: str
    client_secret: str
    password: str
    username: str

    class Config:
        env_prefix = "REDDIT_"


class Settings(BaseSettings):
    pg = PostgresConfig()
    reddit = RedditConfig()
    debug: bool = False
    api_version: str = "/api/v1"
    uri: str = f"postgresql://{pg.user}:{pg.password}@{pg.host}/{pg.db}"
    async_uri: str = f"postgresql+asyncpg://{pg.user}:{pg.password}@{pg.host}/{pg.db}"


settings = Settings()
