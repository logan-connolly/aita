from pydantic import BaseSettings, SecretStr


class ApiConfig(BaseSettings):
    host: str

    class Config:
        env_prefix = "API_"


class RedditConfig(BaseSettings):
    client_id: str
    client_secret: SecretStr
    password: SecretStr
    username: str

    class Config:
        env_prefix = "REDDIT_"


api_settings = ApiConfig()
reddit_settings = RedditConfig()
