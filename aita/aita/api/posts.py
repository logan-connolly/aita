from collections import Counter
from typing import Dict, List, Tuple

import requests

from ..config import api_settings


class ApiPosts:
    """Class for connecting with AITA api.

    :param host: where api is hosted
    """

    def __init__(self, host: str):
        self.url = f"http://{api_settings.host}/api/v1/posts/"
        self.posts = self._posts()

    def _posts(self) -> List[Dict[str, str]]:
        resp = requests.get(self.url)
        if resp.status_code == 200:
            return resp.json()
        return None

    def count_labels(self) -> List[Tuple[str, int]]:
        count = Counter()
        for post in self.posts:
            label = post.get("label")
            count[label] += 1
        return count.most_common()
