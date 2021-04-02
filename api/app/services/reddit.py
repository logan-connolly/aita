from typing import Dict, Optional

from asyncpraw import Reddit
from asyncpraw.models import Submission
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


async def extract_post_info(post: Submission) -> Dict[str, Optional[str]]:
    """Extract information from post needed for training model"""

    def convert_label(flair: str) -> Optional[str]:
        flair_dict = {
            "Asshole": "YTA",
            "Not the A-hole": "NTA",
            "Everyone Sucks": "ESH",
            "No A-holes here": "NAH",
            "Not enough info": "INFO",
        }
        return flair_dict.get(flair)

    return {
        "id": post.id,
        "title": post.title,
        "label": convert_label(post.link_flair_text),
        "text": post.selftext,
    }
