from collections import Counter
from typing import Dict, List, Optional, Tuple

import requests

PostList = List[Dict[str, str]]
PostCounts = List[Tuple[str, int]]


class ApiPosts:
    """Class for connecting with AITA api.
    :param host: where api is hosted
    """

    def __init__(self, host: str):
        self.url = f"http://{host}/api/v1/posts/"

    def posts(self) -> Optional[PostList]:
        """Get posts from api"""
        resp = requests.get(self.url)
        if resp.status_code == 200:
            return resp.json()
        return None

    def count_labels(self) -> Optional[PostCounts]:
        """Count up AITA labels in AITA DB"""
        count: Counter = Counter()
        posts = self.posts()
        if posts:
            for post in posts:
                label = post.get("label")
                count[label] += 1
            return count.most_common()
        return None
