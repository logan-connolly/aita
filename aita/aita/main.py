import typer

from .reddit.config import RedditConfig, connect_reddit
from .reddit.posts import AITA


app = typer.Typer()
config = RedditConfig()
reddit = connect_reddit(config)


@app.command()
def posts(n_posts: int):
    aita = AITA(reddit, n_posts=n_posts)
    typer.echo(aita)


if __name__ == "__main__":
    app()
