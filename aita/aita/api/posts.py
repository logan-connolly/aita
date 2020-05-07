from collections import Counter
from typing import Dict, List

import requests

from ..config import api_settings


class ApiPosts:
    def __init__(self, host: str):
        self.url = f"http://{api_settings.host}/api/v1/posts/"
        self.posts = self._posts()

    def _posts(self) -> List[Dict[str, str]]:
        resp = requests.get(self.url)
        if resp.status_code == 200:
            return resp.json()
        return None

    def count_labels(self):
        cnt = Counter()
        for post in self.posts:
            label = post.get("label")
            cnt[label] += 1
        return cnt.most_common()
