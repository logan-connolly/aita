from collections import Counter

import typer

from praw.models import Submission
from tqdm import tqdm

from .connect import connect_reddit
from .posts import RedditPosts
from ..config import reddit_settings
from ..style import whitespace


reddit = connect_reddit(reddit_settings)
app = typer.Typer()


@app.command()
def add(n_posts: int, category: str = "top") -> None:
    """ Add AITA posts to DB

    --category for selecting "top", "hot" or "new" posts
    """
    rp = RedditPosts(reddit)
    posts = rp.get_posts(n_posts, category)
    count = Counter()
    for i in tqdm(range(n_posts)):
        try:
            post = next(posts)
        except StopIteration:
            break
        tag = handle_post(rp, post)
        count[tag] += 1

    style_output(count)


def handle_post(rp: RedditPosts, post: Submission) -> str:
    """Post to AITA api and return tag based on status code"""
    if post.link_flair_text == "META":
        return "ignored"
    resp = rp.add_to_api(post)
    if resp.status_code == 201:
        return "added"
    if resp.status_code == 400:
        return "existed"
    return "error"


@whitespace(title="Number of AITA posts added to DB:")
def style_output(cnt: Counter) -> None:
    new_posts = typer.style("new post:", fg=typer.colors.GREEN)
    existed = typer.style("existed:", fg=typer.colors.RED)
    ignored = typer.style("ignored:", fg=typer.colors.YELLOW)
    errors = typer.style("errors: ", fg=typer.colors.BRIGHT_RED)
    typer.echo(f"{new_posts}\t {cnt['added']}")
    typer.echo(f"{existed}\t {cnt['existed']}")
    typer.echo(f"{ignored}\t {cnt['ignored']}")
    typer.echo(f"{errors}\t {cnt['error']}")
