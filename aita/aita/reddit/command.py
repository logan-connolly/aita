from collections import Counter

import typer

from tqdm import tqdm

from .connect import connect_reddit
from .posts import RedditPosts
from .style import styled_add
from ..config import reddit_settings

reddit = connect_reddit(reddit_settings)
app = typer.Typer()


@app.command()
def add(n_posts: int, category: str = "top") -> None:
    """Add AITA reddit posts to database via api.
    :param n_posts: how many posts to add to database
    :param category: choose which filter to apply to subreddit
    """
    rp = RedditPosts(reddit)
    posts = rp.get_posts(n_posts, category)

    count = Counter()
    for _, post in tqdm(enumerate(posts)):
        tag = rp.tag_post_status(rp, post)
        count[tag] += 1
    styled_add(count)
