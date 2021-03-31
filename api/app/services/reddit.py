from praw import Reddit

from app.core.config import RedditConfig


def get_reddit_connection(config: RedditConfig) -> Reddit:
    """Function for connecting to reddit with configuration."""
    return Reddit(
        user_agent=f"app by /u/{config.username}",
        client_id=config.client_id,
        client_secret=config.client_secret,
        username=config.username,
        password=config.password,
    )
