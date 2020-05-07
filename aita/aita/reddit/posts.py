import json

from typing import Dict

import requests

from praw import Reddit
from praw.models import Submission
from praw.models.listing.generator import ListingGenerator

from ..config import api_settings


class RedditPosts:
    """Extract posts from /r/AmItheAsshole subreddit"""

    subreddit_name = "AmItheAsshole"
    url = f"http://{api_settings.host}/api/v1/posts/"

    def __init__(self, reddit: Reddit):
        self.reddit = reddit
        self.subreddit = reddit.subreddit(self.subreddit_name)

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(reddit=<Reddit Instance>)"

    def get_posts(self, n_posts: int, category: str = "top") -> ListingGenerator:
        if category not in ("top", "hot", "new"):
            raise ValueError(f"Invalid category: '{category}'")
        if category == "new":
            return self.subreddit.new(limit=n_posts)
        if category == "hot":
            return self.subreddit.hot(limit=n_posts)
        return self.subreddit.top("all", limit=n_posts)

    def add_to_api(self, post: Submission) -> int:
        info = self.extract_post_info(post)
        return requests.post(self.url, data=json.dumps(info))

    def convert_label(self, flair: str) -> str:
        flair_dict = {
            "Asshole": "YTA",
            "Not the A-hole": "NTA",
            "Everyone Sucks": "ESH",
            "No A-holes here": "NAH",
            "Not enough info": "INFO",
        }
        if flair in flair_dict:
            return flair_dict[flair]
        return "NONE"

    def extract_post_info(self, post: Submission) -> Dict[str, str]:
        return {
            "post_id": post.id,
            "title": post.title,
            "label": self.convert_label(post.link_flair_text),
            "text": post.selftext,
        }
