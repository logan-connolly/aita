import json

from typing import Dict

import requests

from praw import Reddit
from praw.models import Submission
from praw.models.listing.generator import ListingGenerator


class AITA:
    """Extract posts from /r/AmItheAsshole subreddit"""

    subreddit = "AmItheAsshole"

    def __init__(self, reddit: Reddit):
        self.reddit = reddit
        self.subreddit = self._subreddit()

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(reddit={self.reddit})"

    def _subreddit(self):
        return self.reddit.subreddit(self.subreddit)

    def posts(self, n_posts: int) -> ListingGenerator:
        return self.subreddit.top("all", limit=n_posts)


def convert_label(flair: str) -> str:
    flair_dict = {
        "Asshole": "YTA",
        "Not the A-hole": "NTA",
        "Everyone Sucks": "ESH",
        "No A-holes here": "NAH",
        "Not enough info": "INFO"
    }
    if flair in flair_dict:
        return flair_dict[flair]
    return "NONE"


def extract_post_info(post: Submission) -> Dict[str, str]:
    return {
        "post_id": post.id,
        "title": post.title,
        "label": convert_label(post.link_flair_text),
        "text": post.selftext
    }


def add_post(post: Submission):
    url = "http://api:8000/api/v1/posts/"
    info = extract_post_info(post)
    payload = json.dumps(info)
    return requests.post(url, data=payload)
