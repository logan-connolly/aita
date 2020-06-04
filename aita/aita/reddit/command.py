from collections import Counter

import typer
from tqdm import tqdm

from .posts import RedditPosts
from .style import styled_add


app = typer.Typer()


@app.command()
def add(host: str, n_posts: int, category: str = "top") -> None:
    """Add AITA reddit posts to database via api.
    :param n_posts: how many posts to add to database
    :param category: choose which filter to apply to subreddit
    """
    config_file = typer.prompt("Path to config")
    rp = RedditPosts(config_file)
    posts = rp.get_posts(n_posts, category)

    count = Counter()
    for _, post in tqdm(enumerate(posts)):
        tag = rp.tag_post_status(host, post)
        count[tag] += 1
    styled_add(count)
