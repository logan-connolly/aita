from pydantic import BaseSettings, SecretStr


class RedditConfig(BaseSettings):
    client_id: str
    client_secret: SecretStr
    password: SecretStr
    username: str
