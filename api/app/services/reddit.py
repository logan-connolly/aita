from asyncpraw import Reddit
from asyncprawcore.exceptions import OAuthException

from app.core.config import RedditConfig, settings


async def get_reddit_connection(config: RedditConfig) -> Reddit:
    """Function for connecting to reddit with configuration."""
    return Reddit(
        user_agent=f"app by /u/{config.username}",
        client_id=config.client_id,
        client_secret=config.client_secret,
        username=config.username,
        password=config.password,
    )


async def get_reddit_user(reddit: Reddit) -> str:
    """Get user object and check that credentials are correct"""
    try:
        user = await reddit.user.me()
        return str(user)
    except OAuthException as err:
        raise ValueError(
            f"Connection failed with username {settings.reddit.username!r}"
        ) from err