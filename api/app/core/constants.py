from enum import Enum

AITA_SUBREDDIT_NAME = "AmItheAsshole"


class AitaLabel(str, Enum):
    """Available labels from Reddit /r/AmITheAsshole"""

    YTA = "YTA"
    NTA = "NTA"
    ESH = "ESH"
    NAH = "NAH"
    NAN = "NAN"
