from enum import Enum


class AitaLabel(str, Enum):
    """Available labels from Reddit /r/AmITheAsshole"""

    # TODO: check if works as well when just ineriting from Enum

    YTA = "YTA"
    NTA = "NTA"
    ESH = "ESH"
    NAH = "NAH"
    INFO = "INFO"
