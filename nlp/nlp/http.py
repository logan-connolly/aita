import requests

from nlp.io import RawPost

PAGE_LIMIT = 50


def get_number_of_pages(api_url: str) -> int:
    """Get number of available posts from info endpoint"""
    resp = requests.get(f"{api_url}/sync/")
    assert resp.status_code == 200, f"Request failed: {resp.url}"
    n_posts = int(resp.json()["posts"])
    return n_posts // PAGE_LIMIT


def fetch_posts(api_url: str) -> list[RawPost]:
    """Fetch posts from running API instance"""
    n_pages = get_number_of_pages(api_url)
    posts = []
    for page_number in range(1, n_pages + 1):
        resp = requests.get(f"{api_url}/posts/?page={page_number}&size={PAGE_LIMIT}")
        assert resp.status_code == 200, f"Request failed: {resp.url}"
        page_posts = resp.json()["items"]
        posts.extend(page_posts)
    return posts
