from enum import Enum

AITA_SUBREDDIT_NAME = "AmItheAsshole"


class AitaLabel(str, Enum):
    """Available labels from Reddit /r/AmITheAsshole"""

    # TODO: check if works as well when just ineriting from Enum

    YTA = "YTA"
    NTA = "NTA"
    ESH = "ESH"
    NAH = "NAH"
    NAN = "NAN"
