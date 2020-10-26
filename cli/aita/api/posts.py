from collections import Counter
from typing import Dict, List, Tuple, Union

import requests


class ApiPosts:
    """Class for connecting with AITA api.
    :param host: where api is hosted
    """

    def __init__(self, host: str):
        self.url = f"http://{host}/api/v1/posts/"

    def posts(self) -> List[Dict[str, str]]:
        resp = requests.get(self.url)
        if resp.status_code == 200:
            return resp.json()
        raise ConnectionError("Could not retrieve posts from API")

    def count_labels(self) -> List[Tuple[str, int]]:
        """Count up AITA labels in AITA DB"""
        count: Counter = Counter()
        for post in self.posts():
            label = post.get("label")
            count[label] += 1
        return count.most_common()
