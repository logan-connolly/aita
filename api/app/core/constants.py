from enum import Enum


class AitaLabel(str, Enum):
    """Available labels from Reddit /r/AmITheAsshole"""

    YTA = "YTA"
    NTA = "NTA"
    ESH = "ESH"
    NAH = "NAH"
    INFO = "INFO"
