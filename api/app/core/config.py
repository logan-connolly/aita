from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresConfig(BaseSettings):
    user: str = "aita"
    password: str = "aita"
    host: str = "localhost"
    db: str = "aita_db"
    model_config = SettingsConfigDict(env_prefix="POSTGRES_")


class RedditConfig(BaseSettings):
    client_id: str
    client_secret: str
    password: str
    username: str
    model_config = SettingsConfigDict(env_prefix="REDDIT_")


class Settings(BaseSettings):
    pg: PostgresConfig = PostgresConfig()
    reddit: RedditConfig = RedditConfig()
    debug: bool = False
    api_version: str = "/api/v1"
    uri: str = f"postgresql://{pg.user}:{pg.password}@{pg.host}/{pg.db}"
    async_uri: str = f"postgresql+asyncpg://{pg.user}:{pg.password}@{pg.host}/{pg.db}"


settings = Settings()
