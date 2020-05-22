import json

from typing import Dict

import requests

from praw import Reddit
from praw.models import Submission
from praw.models.listing.generator import ListingGenerator

from ..config import api_settings


class RedditPosts:
    """Extract posts from /r/AmItheAsshole subreddit.
    :param reddit: connection object with valid credentials
    """

    subreddit_name = "AmItheAsshole"
    url = f"http://{api_settings.host}/api/v1/posts/"

    def __init__(self, reddit: Reddit):
        self.reddit = reddit
        self.subreddit = reddit.subreddit(self.subreddit_name)

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(reddit=<Reddit Instance>)"

    def get_posts(self, n_posts: int, category: str = "top") -> ListingGenerator:
        """Get AITA posts from reddit.
        :param n_posts: number of reddit posts to extract.
        :param category: choose "top", "hot" or "new" posts
        """
        if category not in ("top", "hot", "new"):
            raise ValueError(f"Invalid category: '{category}'")
        if category == "new":
            return self.subreddit.new(limit=n_posts)
        if category == "hot":
            return self.subreddit.hot(limit=n_posts)
        return self.subreddit.top("all", limit=n_posts)

    def add_to_api(self, post: Submission) -> int:
        """Add reddit post to AITA api and get status code.
        :param post: AITA reddit post.
        """
        info = self.extract_post_info(post)
        resp = requests.post(self.url, data=json.dumps(info))
        return resp.status_code

    def convert_label(self, flair: str) -> str:
        """Extract flair from AITA post and convert to label in DB.
        :param flair: tag given to AITA posts on reddit
        """
        flair_dict = {
            "Asshole": "YTA",
            "Not the A-hole": "NTA",
            "Everyone Sucks": "ESH",
            "No A-holes here": "NAH",
            "Not enough info": "INFO",
        }
        return flair_dict.get(flair, "NONE")

    def extract_post_info(self, post: Submission) -> Dict[str, str]:
        """Extract AITA post text and metadata
        :param post: extract information from post to pass as payload to api
        """
        return {
            "post_id": post.id,
            "title": post.title,
            "label": self.convert_label(post.link_flair_text),
            "text": post.selftext,
        }

    def tag_post_status(self, post: Submission) -> str:
        """Post to AITA api and return tag based on status code.
        :param post: reddit post submission from AITA subreddit
        """
        if post.link_flair_text == "META":
            return "ignored"

        resp = self.add_to_api(post)
        if resp.status_code == 201:
            return "added"
        if resp.status_code == 400:
            return "existed"
        return "error"
