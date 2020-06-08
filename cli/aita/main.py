import typer

from aita.api.commands import app as api_app
from aita.reddit.commands import app as reddit_app


app = typer.Typer()
app.add_typer(api_app, name="api")
app.add_typer(reddit_app, name="reddit")


if __name__ == "__main__":
    app()
