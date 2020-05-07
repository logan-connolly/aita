import typer

from aita.reddit.config import RedditConfig, connect_reddit
from aita.reddit.posts import AITA, add_post


app = typer.Typer()
config = RedditConfig()
reddit = connect_reddit(config)


@app.command()
def posts(n_posts: int = 5):
    posts = AITA(reddit).posts(n_posts)
    for _ in range(n_posts):
        post = next(posts)
        if post.link_flair_text != "META":
            resp = add_post(post)
            typer.echo(resp)


@app.command()
def counts():
    typer.echo("count labels")


if __name__ == "__main__":
    app()
