from pydantic import BaseSettings


class PostgresSettings(BaseSettings):
    user: str
    password: str
    host: str
    db: str

    class Config:
        env_prefix = "POSTGRES_"


class Settings(BaseSettings):
    DEBUG: bool = True

    API_TITLE: str = "AITA"
    API_V1_STR: str = "/api/v1"
    OPENAPI_URL: str = f"{API_V1_STR}/openapi.json"

    MODEL_PATH: str = "example/path"

    PG = PostgresSettings()
    URI: str = f"postgres://{PG.user}:{PG.password}@{PG.host}/{PG.db}"

    class Config:
        case_sensitive = True


settings = Settings()
