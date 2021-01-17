from pydantic import BaseSettings


class RedditConfig(BaseSettings):
    client_id: str
    client_secret: str
    password: str
    username: str

    class Config:
        env_prefix = "REDDIT_"
