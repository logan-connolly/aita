from praw import Reddit

from ..config import RedditConfig


def connect_reddit(settings: RedditConfig):
    """Function for connecting to reddit with configuration.

    :param settings: reddit configuration needed to connect with reddit via praw
    """
    return Reddit(
        user_agent=f"app by /u/{settings.username}",
        client_id=settings.client_id,
        client_secret=settings.client_secret.get_secret_value(),
        password=settings.password.get_secret_value(),
        username=settings.username,
    )
